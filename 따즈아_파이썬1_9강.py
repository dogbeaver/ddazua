''' 변수(variable)
 :변수는 객체를 가리키고 있는 것이다. 참조변수라고 한다.

aa = 100

bb = 100

is (파이썬의 내장함수)를 이용해서 두개의 변수가
서로 같은 값을 갖고 있는 지 파악할 수 있다.

aa is bb
'''

aa = 100
bb = 100
cc = 100

print(aa is bb)

#변수 삭제하기
del(aa)

#변수 선언 및 초기화
cc = dd = 100 #여러개의 변수에 동일 값을 대입한다.

cc, dd = "국제시장", "명량"

print(cc)
print(dd)

(cc, dd) = ("aa", "bb")
print(cc)

[cc, dd] = ["하이","파이썬!!"]

print(cc)
print(dd)

#데이터의 복사하는데 있어서 혼동하기 쉬운 예
aa = ["a","b","c"]

bb = aa

aa[2] = "d"

print(aa)
print(bb)

#데이터의 복사
aa = ["a","b","c"]
bb = aa[:] #aa의 리스트를 처음부터 끝가지 슬라이싱
aa[2] = "d"
print(aa)
print(bb)












