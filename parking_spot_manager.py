class parking_spot:
    # 주차장 초기화
    def __init__(self, name, city, district, ptype, longitude, latitude):
        # 정보 저장
        self.__item = {'name': name, 'city': city, 'district': district, 'ptype': ptype, 'longitude': float(longitude), 'latitude': float(latitude)}

    def get(self, keyword='name'):
        # 주차장 정보를 가져옴
        return self.__item.get(keyword)

    def __str__(self):
        # 주차장 정보를 문자열로 표현함
        item = self.__item
        s = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']} "
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s


def str_list_to_class_list(str_list):
    # 문자열 리스트를 객체 리스트로 변환함
    return [parking_spot(*s.split(',')[1:]) for s in str_list]


def print_spots(spots):
    # 출력하는 함수
    print(f"---print elements({len(spots)})---")
    for spot in spots:
        print(spot)


def filter_by_name(spots, name):
    # 이름으로 필터링
    return [spot for spot in spots if name in spot.get('name')]


def filter_by_city(spots, city):
    #도시로 필터링
    return [spot for spot in spots if city in spot.get('city')]


def filter_by_district(spots, district):
    # 지역구로 필터링
    return [spot for spot in spots if district in spot.get('district')]


def filter_by_ptype(spots, ptype):
    # 타입으로 필터링
    return [spot for spot in spots if ptype in spot.get('ptype')]


def filter_by_location(spots, locations):
    # 위치로 필터링
    min_lat, max_lat, min_long, max_long = locations
    return [spot for spot in spots if min_lat < spot.get('latitude') < max_lat and min_long < spot.get('longitude') < max_long]


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    spots = filter_by_district(spots, '동작')
    print_spots(spots)

    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)



