# HASH -> python : dict()

 - 평균적으로 O(1)의 효율적인 알고리즘
 - but 동일한 index 에 다른 여러개의 값으로 충돌 시 최악의 경우 O(n)

--- 
## 해시 테이블
 - 해시 함수로 값을 키로 매핑 후 해시값으로 데이터와 함께 저장하는 자료구조
 - 장점 : 메모리 효울적 / 단점 : 충돌 잦음
 - Key -> (hash funcion) -> 정해진 hash index 주소에 bucket에 값이 저장

## 해시 테이블 충돌 해결
#### 체이닝 (평균 O(1) 최악 O(n))
 - 동일 인덱스 버킷 내 충돌 시 연결 리스트로 다음 값 저장 

#### 개방번지
 - 해시 버킷에 1개 저장하지만, 충돌 시 다른 주소에 저장 허용
   1. 선형탐사 -> 고정 폭에 엑세스(n칸 뒤에 삽입, 삭제, 탐색) -> 데이터가 몰림(clustering)
   2. 제곱탐사 -> 폭^2에 엑세스(n^2칸 뒤에 삽입, 삭제, 탐색) -> 데이터가 몰림(clustering)
   3. 이중해싱 -> 탐색 규칙을 없애 클러스터링을 없앰

--- 
## Direct Address table 
 - 키의 전체 구조와 동일한 크기의 해시 버킷 생성
 - 장점: 충돌 없음 / 단점 : 메모리 비효율적