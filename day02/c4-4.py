# p.251
numbers = [ 103, 52, 273, 32, 77 ]
print( min( numbers )) # min(리스트) 최솟값
print( max( numbers )) # max(리스트) 최댓값
print( sum( numbers )) # sum(리스트) 합계

# p.252 reversed(리스트)
numbers_reversed = reversed(numbers) # 리스트 뒤집기
print( numbers_reversed )
print( next( numbers_reversed ) )
print( list( numbers_reversed ) )
# int( ) float( ) str( ) list( ) : 특정 타입으로 변환 함수

# 이터러블 : 요소들을 하나씩 차례로 꺼내기 가능한 객체 의미
# 이터레이터 : 이터러블 중에서 하나씩 차례로 빼낼 수 있는 요소
