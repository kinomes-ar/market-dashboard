# 한국 오전 동향 (kr_morning)
이 작업은 GitHub Actions 러너에서 실행된다. 저장소(kinomes-ar/market-dashboard, 사이트 limnkim.fyi)는 현재 디렉터리에 이미 체크아웃되어 있다. index.html을 직접 편집하면 되고, git 커밋·푸시는 워크플로우가 자동으로 하므로 하지 않는다. 러너는 네트워크가 자유로우므로 시세는 워커를 curl로 직접 호출한다(항상 URL 끝에 &cb=<현재유닉스초> 추가). 시각은 UTC 기준. 편집은 python3 re.sub로 마커/영역만 정확히 치환하고, 각 치환 후 assert로 검증한다. 실패하면 index.html을 건드리지 말고 종료한다(워크플로우가 변경 없음을 감지해 커밋 안 함). 뉴스·서술은 WebSearch로 실제 기사만 근거로 하고 지어내지 않는다. 숫자·방향은 워커 값과 반드시 일치.

시세: /kr 워커(kr_close와 동일 URL). updated 30분 이내 필수. 한국 개장 전(00:00 UTC 이전)이거나 낡으면 종료.

수정 허용: 한국 카드 <div class="pane morning">의 morning-list ko/en(핵심 3~4개 <li>), <b class="mupd" data-mkt="kr"> data-iso, 타일 .tile[data-kr] .val·.chg, 헤더 <b class="upd" data-mkt="kr"> data-iso, 요약 SUMKR_KO/EN + summary data-iso.
**<b class="iupd" data-mkt="kr">는 절대 금지(마감 전용).** '주요 이슈' 탭(pane issue) 금지. 마커 assert.
