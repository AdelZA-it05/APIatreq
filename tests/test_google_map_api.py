import json
from utils.api import Google_maps_api
from requests import Response
from utils.checking import Checking
import allure


@allure.epic('Test create place')
class Test_create_place():
    """Класс содержащий тест по работе с локацией"""

    @allure.description('Test create, update, delete place')
    def test_create_new_place(self):
        """Тест по созданию, изменние и удаление новой локации"""

        print("Метод POST")
        result_post: Response = Google_maps_api.create_new_place()  # вызов метода по созданию новой локации
        check_post = result_post.json()
        place_id = check_post.get("place_id")  # получения place_id для метода GET
        Checking.check_status_code(result_post, 200)  # вызов метода по проверке статус-кода
        Checking.check_json_fields(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print("Метод GET POST")
        result_get = Google_maps_api.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 200)  # вызов метода по проверке статус-кода
        Checking.check_json_fields(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        print("Метод PUT")
        result_put = Google_maps_api.put_new_place(place_id)  # отправка метода Put
        Checking.check_status_code(result_put, 200)  # вызов метода по проверке статус-кода
        Checking.check_json_fields(result_put, ['msg'])

        print("Метод GET PUT")
        result_get = Google_maps_api.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 200)  # вызов метода по проверке статус-кода

        print("Метод DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)  # удаление данных о созданной локации
        Checking.check_status_code(result_delete, 200)  # вызов метода по проверке статус-кода

        print("Метод GET DELETE")
        result_get = Google_maps_api.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 404)  # вызов метода по проверке статус-кода
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')


