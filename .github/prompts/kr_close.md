# 한국 마감 갱신 (kr_close)
이 작업은 GitHub Actions 러너에서 실행된다. 저장소(kinomes-ar/market-dashboard, 사이트 limnkim.fyi)는 현재 디렉터리에 이미 체크아웃되어 있다. index.html을 직접 편집한 뒤, 변경이 있으면 반드시 직접 배포까지 한다: git add index.html && git commit -m "auto: <작업id> update" && git push origin main (push 실패 시 git pull --rebase origin main 후 최대 3회 재시도). git 인증은 액션이 이미 구성해뒀으므로 그대로 push하면 된다. 변경이 없으면 커밋하지 않는다. 러너는 네트워크가 자유로우므로 시세는 워커를 curl로 직접 호출한다(항상 URL 끝에 &cb=<현재유닉스초> 추가). 시각은 UTC 기준. 편집은 python3 re.sub로 마커/영역만 정확히 치환하고, 각 치환 후 assert로 검증한다. 실패하면 index.html을 건드리지 말고 종료한다(워크플로우가 변경 없음을 감지해 커밋 안 함). 뉴스·서술은 WebSearch로 실제 기사만 근거로 하고 지어내지 않는다. 숫자·방향은 워커 값과 반드시 일치.

시세: curl "https://fmp-movers.kinomeartemis.workers.dev/kr?index=KOSPI,KOSDAQ&stocks=005930,000660&cb=<유닉스초>" → index[]·stocks[]의 price·changePct 사용(코스피/코스닥/삼성전자 005930/SK하이닉스 000660). updated가 30분 이상 낡으면 cb 바꿔 1회 재시도, 그래도 낡으면 종료.

수정 허용 범위(그 외 절대 금지 — 미국·중국 카드, 실시간 <script>, 레딧, 버전 등):
- 한국 카드 타일 .tile[data-kr="KOSPI"|"KOSDAQ"|"005930"|"000660"]의 .val(지수 콤마 2자리, 종목 ₩+정수 콤마)·.chg(상승 chg up ▲ +x.xx% / 하락 chg down ▼ -x.xx%)
- 한국 카드(이중언어): 핵심 이슈 ul[data-lang=ko]/[data-lang=en], 읽는 법 p ko/en, h4·signal ko/en span — 마감 종가 기준으로 갱신
- 헤더 <b class="upd" data-mkt="kr"> data-iso = 현재 UTC ISO8601Z. <b class="iupd" data-mkt="kr"> data-iso도 동일 시각으로(마감 전용 시각).
- 요약 한국 줄: <!--SUMKR_KO-->…<!--/SUMKR_KO-->와 <!--SUMKR_EN-->…<!--/SUMKR_EN--> 사이를 오늘 마감 한 줄로(한국어 <b>한국</b> — …, 영어 <b>Korea</b> — …, 등락은 <span class="up">/"down"). 요약 헤더 data-mkt="summary" data-iso 현재 UTC.
뉴스는 WebSearch 2~3회(원/달러, 수급, 금통위, 핵심 3~4건). 완료 후 마커 쌍 존재 assert.
