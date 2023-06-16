
import file_manager
import parking_spot_manager


def start_process(path):
    # 파일에서 문자열 리스트를 가져온다
    str_list = file_manager.read_file(path)
    # 문자열 리스트를 parking_spot 객체 리스트로 변환한다
    spots = parking_spot_manager.str_list_to_class_list(str_list)

    while True:
        # 메뉴 선택 
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        # 메뉴 선택을 입력받음
        select = int(input('type:'))

        if select == 1:
            # parking_spot 객체 리스트를 출력한다
            parking_spot_manager.print_spots(spots)

        elif select == 2:
            # 필터 기능
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            
            # 사용자가 어떤 옵션을 선택했는지 물어봄
            select = int(input('type:'))
            
            if select == 1:
                #이름
                keyword = input('type name:')
                spots = parking_spot_manager.filter_by_name(spots, keyword)
                
            elif select == 2:
                #도시
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword)
                
            elif select == 3:
                #지역구
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword)
                
            elif select == 4:
                #타입
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword)
                
            elif select == 5:
                #위치
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                locations = (min_lat, max_lat, min_lon, max_lon)
                spots = parking_spot_manager.filter_by_location(spots, locations)
                
            else:
                print("invalid input")

        elif select == 3:
            # 정렬 기능 
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')

            # 키워드가 유효한가?
            if keyword in keywords:
                # 유효한 경우
                spots = parking_spot_manager.sort_by_keyword(spots, keyword)
            else:
                # 잘못된 모임
                print("invalid input")

        elif select == 4:
            # 프로그램 종료
            print("Exit")
            break

        else:
            # 잘못된 입력
            print("invalid input")













