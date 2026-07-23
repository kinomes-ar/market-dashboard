#!/usr/bin/env python3
# 워커에서 미·한·중 지수/대형주 시세를 받아 quotes.json 으로 저장 (GitHub Actions에서 실행)
import json, time, datetime, urllib.request
CB=str(int(time.time()))
BASE="https://fmp-movers.kinomeartemis.workers.dev"
def get(path):
    req=urllib.request.Request(BASE+path+("&" if "?" in path else "?")+"cb="+CB, headers={"User-Agent":"gh-actions-quotes"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))
q=get("/quotes?symbols=^GSPC,^IXIC,^DJI,000001.SS,399001.SZ,^HSI")
k=get("/kr?index=KOSPI,KOSDAQ&stocks=005930,000660")
qm={x["symbol"]:x for x in q.get("quotes",[])}
km={x["code"]:x for x in (k.get("index",[])+k.get("stocks",[]))}
def qv(s):
    d=qm.get(s)
    return None if not d or d.get("price") is None else {"price":round(d["price"],2),"changePct":round(d["changePct"],2),"prevClose":round(d.get("prevClose") or 0,2),"ts":d.get("ts")}
def kv(c):
    d=km.get(c)
    return None if not d or d.get("price") is None else {"price":d["price"],"changePct":round(d["changePct"],2)}
out={
 "updated":datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
 "worker_updated_q":q.get("updated"),
 "worker_updated_kr":k.get("updated"),
 "us":{"gspc":qv("^GSPC"),"ixic":qv("^IXIC"),"dji":qv("^DJI")},
 "kr":{"kospi":kv("KOSPI"),"kosdaq":kv("KOSDAQ"),"samsung":kv("005930"),"hynix":kv("000660")},
 "cn":{"sse":qv("000001.SS"),"szse":qv("399001.SZ"),"hsi":qv("^HSI")},
}
assert out["us"]["gspc"] and out["kr"]["kospi"] and out["cn"]["sse"], "missing core quotes"
json.dump(out, open("quotes.json","w"), ensure_ascii=False, indent=2)
print("wrote quotes.json @", out["updated"])
