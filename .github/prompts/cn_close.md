# 중국 마감 갱신 (cn_close)
이 작업은 GitHub Actions 러너에서 실행된다. 저장소(kinomes-ar/market-dashboard, 사이트 limnkim.fyi)는 현재 디렉터리에 이미 체크아웃되어 있다. index.html을 직접 편집하면 되고, git 커밋·푸시는 워크플로우가 자동으로 하므로 하지 않는다. 러너는 네트워크가 자유로우므로 시세는 워커를 curl로 직접 호출한다(항상 URL 끝에 &cb=<현재유닉스초> 추가). 시각은 UTC 기준. 편집은 python3 re.sub로 마커/영역만 정확히 치환하고, 각 치환 후 assert로 검증한다. 실패하면 index.html을 건드리지 말고 종료한다(워크플로우가 변경 없음을 감지해 커밋 안 함). 뉴스·서술은 WebSearch로 실제 기사만 근거로 하고 지어내지 않는다. 숫자·방향은 워커 값과 반드시 일치.

시세: curl "https://fmp-movers.kinomeartemis.workers.dev/quotes?symbols=000001.SS,399001.SZ,^HSI&cb=<유닉스초>" → price·changePct(상하이종합/선전성분/항셍). 신선도 30분, 낡으면 재시도 후 종료.

수정 허용 범위(그 외 금지):
- 중국 카드(#sec-cn) 타일: 라벨 '상하이종합/선전성분/항셍' 타일(.tile[data-cn] 속성 있음: 000001.SS/399001.SZ/^HSI)의 .val·.chg
- 중국 카드(이중언어) 핵심 이슈·읽는 법·h4·signal ko/en
- 헤더 <b class="upd" data-mkt="cn"> data-iso 현재 UTC, <b class="iupd" data-mkt="cn"> data-iso도 동일 시각
- 요약 중국 줄 <!--SUMCN_KO-->·<!--SUMCN_EN--> 사이 + summary data-iso
뉴스: PBOC·위안화·부동산·미중 등 2~3회. 마커 assert.
