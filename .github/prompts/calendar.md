# 경제 캘린더 (calendar)
이 작업은 GitHub Actions 러너에서 실행된다. 저장소(kinomes-ar/market-dashboard, 사이트 limnkim.fyi)는 현재 디렉터리에 이미 체크아웃되어 있다. index.html을 직접 편집하면 되고, git 커밋·푸시는 워크플로우가 자동으로 하므로 하지 않는다. 러너는 네트워크가 자유로우므로 시세는 워커를 curl로 직접 호출한다(항상 URL 끝에 &cb=<현재유닉스초> 추가). 시각은 UTC 기준. 편집은 python3 re.sub로 마커/영역만 정확히 치환하고, 각 치환 후 assert로 검증한다. 실패하면 index.html을 건드리지 말고 종료한다(워크플로우가 변경 없음을 감지해 커밋 안 함). 뉴스·서술은 WebSearch로 실제 기사만 근거로 하고 지어내지 않는다. 숫자·방향은 워커 값과 반드시 일치.

수정 허용: <div id="calBody"> 내부와 #calAsof 텍스트만. 이중언어(cal-day/cal-date/cal-ev 구조, 모든 텍스트 ko/en span 두 벌, 고임팩트 <span class="hi">★). 오늘(현지 상하이 기준)부터 이번 주말까지 + '다가오는 일정' 블록. WebSearch로 미(지표·FOMC·실적)/한(금통위·수출·물가)/중(PMI·LPR·정책) 2~3회. #calBody 존재 assert.
