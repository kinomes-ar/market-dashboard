# 이번 주 전망 (week_outlook, 월요일)
이 작업은 GitHub Actions 러너에서 실행된다. 저장소(kinomes-ar/market-dashboard, 사이트 limnkim.fyi)는 현재 디렉터리에 이미 체크아웃되어 있다. index.html을 직접 편집하면 되고, git 커밋·푸시는 워크플로우가 자동으로 하므로 하지 않는다. 러너는 네트워크가 자유로우므로 시세는 워커를 curl로 직접 호출한다(항상 URL 끝에 &cb=<현재유닉스초> 추가). 시각은 UTC 기준. 편집은 python3 re.sub로 마커/영역만 정확히 치환하고, 각 치환 후 assert로 검증한다. 실패하면 index.html을 건드리지 말고 종료한다(워크플로우가 변경 없음을 감지해 커밋 안 함). 뉴스·서술은 WebSearch로 실제 기사만 근거로 하고 지어내지 않는다. 숫자·방향은 워커 값과 반드시 일치.

수정 허용: <!--WKOUT_KO-->·<!--WKOUT_EN--> 사이(각 5개 <li>: 이번주핵심/한국/중국/미국/관전, 전향적 어조, 등락 span.up/down, 핵심 <b>), 헤더 <b class="upd" data-mkt="weekoutlook"> data-iso, 푸터 버전 셋째자리 +1(예 V2.443→V2.4431 방식: 소수부 2자리 초과분 증가).
재료: WebSearch 2~4회(지난주 마감 3국, 주말 뉴스, 이번 주 일정). 직전 수치는 카드 베이크값과 일치. 마커 assert.
