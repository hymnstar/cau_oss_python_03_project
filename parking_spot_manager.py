class parking_spot:
    def __init__(self, name, city, district, ptype, longitude, latitude):
        # 주차장 정보를 딕셔너리로 저장한다
        self.__item = {'name': name, 'city': city, 'district': district, 'ptype': ptype, 'longitude': float(longitude), 'latitude': float(latitude)}

    def get(self, keyword='name'):
        # 특정 정보를 가져온다
        return self.__item.get(keyword)

    def __str__(self):
        # 주차장 정보를 깔끔한 문자열로 표시 
        item = self.__item
        s = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']} "
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s


def str_list_to_class_list(str_list):
    # 문자열 리스트를 객체 리스트로 변환한다
    class_list = []
    for s in str_list:
        items = s.split(',')
        class_list.append(parking_spot(items[1], items[2], items[3], items[4], items[5], items[6]))
    return class_list


def print_spots(spots):
    # 객체 리스트를 출력
    print(f"---print elements({len(spots)})---")
    for spot in spots:
        print(spot)


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    #version#2
    import file_manager
    str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)

    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)
