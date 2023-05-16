
def SearchAdress(AddressList,Find=0,AddressNum=1,AddressGet=1):
    if Find != 0:
        if AddressGet == 1:
            Address=[list(set([i[AddressGet] for i in AddressList if Find in i[AddressNum]])) if j == 1 else list(set([i[AddressGet][0:2] for i in AddressList if Find in i[AddressNum]])) for j in range(2)]
            return Address
        elif AddressGet == 3 or AddressGet == 5:
            Address=[list(set([i[AddressGet] for i in AddressList if Find in i[AddressNum]])) if j == 1 else list(set([i[AddressGet][:-1] for i in AddressList if Find in i[AddressNum]])) for j in range(2)]
            return Address
        else:
            Address=list(set([i[AddressGet] for i in AddressList if Find in i[AddressNum]]))
            return Address
    
    elif Find == 0:
        if AddressGet == 1:
            CityList=[list(set([i[AddressGet] for i in AddressList])) if j == 1 else list(set([i[AddressGet][0:2] for i in AddressList])) for j in range(2)]
            return CityList
        elif AddressGet == 3 or AddressGet == 5:
            DorTList=[list(set([i[AddressGet] for i in AddressList])) if j == 1 else list(set([i[AddressGet][:-1] for i in AddressList])) for j in range(2)]
            return DorTList
        else:
            RorNList=list(set([i[AddressGet] for i in AddressList]))
            return RorNList
        
#탐색하는 데이터의 위치 (판별대상)
FIND2CITY=1
FIND2DISTRICT=3
FIND2TOWN=5
FIND2ROAD=7
FIND2NUM=10

#리스트로 얻고자 하는 데이터의 종류 (출력대상)
FIND_CITY=1
FIND_DISTRICT=3
FIND_TOWN=5
FIND_ROAD=7
FIND_NUM=10

# TODO 1 : 핵심 단어만 리스트화하는 함수 만들기
#  EX)서울 특별시 -> 서울 ,강원도 -> 강원
#  방식은 서울 특별시와 같은 리스트를 넣으면 변환된 리스트가 나오게 하는 함수를 새로 만들거나
#  기존 함수에 플래그 인수 추가 중 선택
#  SearchAdress(AddressList,"경상북도",0)  # 출력 : 서울 특별시 , 강원도, 제주특별자치도
#  SearchAdress(AddressList,"경상북도",1)  # 출력 : 서울,강원,대구

f = open("PythonSource/Util/Address.txt", "r", encoding="utf-8")
AddressList=[i.split("|") for i in f.readlines()]
f.close()

CityList=SearchAdress(AddressList,AddressGet=FIND_CITY)
print(CityList)

CityList=SearchAdress(AddressList,Find="강서구",AddressNum=FIND_DISTRICT,AddressGet=FIND_CITY)
print(CityList)

DistrictList=SearchAdress(AddressList,AddressGet=FIND_DISTRICT)
print(DistrictList)

DistrictList=SearchAdress(AddressList,Find="서울",AddressNum=FIND2CITY,AddressGet=FIND_DISTRICT)
print(DistrictList)

TownList=SearchAdress(AddressList,AddressGet=FIND_TOWN)
print(TownList)

TownList=SearchAdress(AddressList,Find="금산군",AddressNum=FIND2DISTRICT,AddressGet=FIND_TOWN)
print(TownList)

RoadList=SearchAdress(AddressList,AddressGet=FIND_ROAD)
print(RoadList)

RoadList=SearchAdress(AddressList,Find="강동구",AddressNum=FIND2DISTRICT,AddressGet=FIND_ROAD)
print(RoadList)

# NumList=SearchAdress(AddressList,AddressGet=FIND_NUM)
# print(NumList)

NumList=SearchAdress(AddressList,Find="금산군",AddressNum=FIND2DISTRICT,AddressGet=FIND_NUM)
print(NumList)