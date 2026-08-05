# 미국 마감·요약·레딧 갱신 (us_close)
이 작업은 GitHub Actions 러너에서 실행된다. 저장소(kinomes-ar/market-dashboard, 사이트 limnkim.fyi)는 현재 디렉터리에 이미 체크아웃되어 있다. index.html을 직접 편집하면 되고, git 커밋·푸시는 워크플로우가 자동으로 하므로 하지 않는다. 러너는 네트워크가 자유로우므로 시세는 워커를 curl로 직접 호출한다(항상 URL 끝에 &cb=<현재유닉스초> 추가). 시각은 UTC 기준. 편집은 python3 re.sub로 마커/영역만 정확히 치환하고, 각 치환 후 assert로 검증한다. 실패하면 index.html을 건드리지 말고 종료한다(워크플로우가 변경 없음을 감지해 커밋 안 함). 뉴스·서술은 WebSearch로 실제 기사만 근거로 하고 지어내지 않는다. 숫자·방향은 워커 값과 반드시 일치.

시세: curl "https://fmp-movers.kinomeartemis.workers.dev/quotes?symbols=^GSPC,^IXIC,^DJI&cb=<유닉스초>" → price·changePct·prevClose(S&P/나스닥/다우). 미국 마감 직후 실행이므로 ts가 마감 시각 근처면 정상.

수정 허용 범위: (1) <!-- USA --> 섹션·헤더 <b class="upd" data-mkt="us"> data-iso, 미국 타일 .tile[data-us], (2) 상단 .summary(sflow ko/en 5개 <li>: 핵심/한국/중국/미국/관전 — **마커 4쌍 보존 필수**: <li><!--SUMKR_KO--><b>한국</b> — …<!--/SUMKR_KO--></li>, SUMCN_KO, SUMKR_EN, SUMCN_EN 동일 패턴; flow 태그 ko/en; summary data-iso), (3) REDDIT 배열(10개 {tk,nm,nmEn,sent,desc,descEn,posts:[{ups,t,tEn}×3]}).
실시간 미국 주식 <script> 블록(FMP·카운트다운·nxt)과 한·중 카드는 금지. 버전 안 올림.
REDDIT 수정 후 반드시: 첫 <script> 블록을 추출해 node --check로 문법 검증, 실패 시 원복·종료. 마커 4쌍 assert.
뉴스: 연준·금리·유가·빅테크 3~4건 + 레딧 화제(AltIndex/ApeWisdom 참고) WebSearch.
