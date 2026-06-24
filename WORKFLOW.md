# WORKFLOW — 작업 규칙

진본(source of truth)은 이 GitHub 저장소 `kinomes-ar/market-dashboard` 입니다.
배포: GitHub Pages → https://limnkim.fyi

## 황금 규칙
**편집 전 최신을 받고(pull), 끝나면 바로 올린다(push).**
로컬 파일을 진본으로 신뢰하지 말 것 — 자동화나 다른 컴퓨터가 그새 바꿔 올렸을 수 있음.

## Cowork(클로드)로 작업할 때
에이전트는 다음을 자동으로 한다(프로젝트 지시문에 규칙이 있어야 함):
1. 시작 시 저장소 최신 `index.html`을 받아 Analysis 폴더(`index.html` / `market-dashboard.html`)에 덮어쓴다.
2. 그 위에서 편집한다.
3. 끝나면 같은 저장소에 push한다.

주의: git 작업은 `/tmp`에서 한다(마운트 폴더는 잠금 오류). force-push·fresh init 금지 — favicon, CNAME, site.webmanifest, 아이콘 등 루트 파일을 보존한다. 토큰은 자동화와 동일한 fine-grained PAT(Contents Read/Write).

## 직접(에디터 + git)으로 작업할 때
1. `git pull`
2. 편집
3. `git add -A && git commit -m "..." && git push`

## 자동화 (메인 컴퓨터)
예약 작업이 장 마감 기준으로 카드/레딧을 갱신하고 push한다 — 상하이 시간 기준: 중국 15:20, 한국 14:56, 미국 화~토 05:34, 주간 토 06:08.

## 두 컴퓨터 동시 편집 주의
같은 줄을 동시에 고치지만 않으면 충돌은 거의 없다. 항상 "먼저 pull, 끝나면 push".
