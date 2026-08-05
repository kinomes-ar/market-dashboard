# 중국 오전 동향 (cn_morning)
이 작업은 GitHub Actions 러너에서 실행된다. 저장소(kinomes-ar/market-dashboard, 사이트 limnkim.fyi)는 현재 디렉터리에 이미 체크아웃되어 있다. index.html을 직접 편집한 뒤, 변경이 있으면 반드시 직접 배포까지 한다: git add index.html && git commit -m "auto: <작업id> update" && git push origin main (push 실패 시 git pull --rebase origin main 후 최대 3회 재시도). git 인증은 액션이 이미 구성해뒀으므로 그대로 push하면 된다. 변경이 없으면 커밋하지 않는다. 러너는 네트워크가 자유로우므로 시세는 워커를 curl로 직접 호출한다(항상 URL 끝에 &cb=<현재유닉스초> 추가). 시각은 UTC 기준. 편집은 python3 re.sub로 마커/영역만 정확히 치환하고, 각 치환 후 assert로 검증한다. 실패하면 index.html을 건드리지 말고 종료한다(워크플로우가 변경 없음을 감지해 커밋 안 함). 뉴스·서술은 WebSearch로 실제 기사만 근거로 하고 지어내지 않는다. 숫자·방향은 워커 값과 반드시 일치.

시세: /quotes 워커(cn_close와 동일 URL). updated 30분 이내. 중국 본장 개장 전(01:30 UTC 이전)이면 종료.

수정 허용: 중국 카드 pane morning의 morning-list ko/en, <b class="mupd" data-mkt="cn"> data-iso, 타일 .val·.chg, 헤더 upd data-iso, 요약 SUMCN_KO/EN + summary data-iso.
**iupd 금지(마감 전용).** pane issue 금지. 마커 assert.
