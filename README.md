# todo api server
>dockerized postgresql

async 방식으로 데이터 베이스를 엑세스를 하는 간단한 예제입니다.
non-blocking IO로 멀티 리퀘스트 처리에 유리합니다.

## 실행방법
- 가상환경을 만들고 activate한다.
- pip install -r requirement.txt - 필요한 패키지를 설치한다.
- docker compose up 명령으로 postgresql을 docker로 실행한다.
- uvicorn main:app --reload
- localhost:8000/docs 로 확인한다.

