from lib2to3.pgen2.token import NUMBER
import requests
import pytest



def test_status_login():
    url = 'https://k-ampus.dev/api/v1/login'
    response = requests.post(url, json={
    "username":"skhalipa@gmail.com",
    "password":"skhalipa@gmail.com"
})
#  1. Тест, что статус операции, которую возвращает бэкенд равна 200    
    assert response.status_code == 200 
#  2. Тест, что объект json содержит поле accessToken и данное поле не пустое    
    assert 'accessToken' in response.json() 
    assert response.json()['accessToken'] != ""

  
def test_status_competence():
    url = 'https://k-ampus.dev/api/v1/login'
    response = requests.post(url, json={
    "username":"skhalipa@gmail.com",
    "password":"skhalipa@gmail.com"
 })   
    aToken  = response.json()['accessToken']
    url2 = 'https://k-ampus.dev/api/v1/competence'
    response = requests.get(url2, headers={"Authorization":aToken})
#  1.1. Тест, что статус операции, которую возвращает бэкенд равна 200       
    assert response.status_code == 200
#  1.2. Тест, что json содержит объект content и данный объект является массивом    
    assert 'content' in response.json()
    assert type(response.json()['content']) is list
#  2. Тест, что объект content не является пустым    
    assert response.json()['content'] != ""
#  3. Тест, что каждый элемент массива content, является:
    #  a. id — Number
    assert type(response.json()['content'][0]['id']) is int
    #  b. name — String
    assert type(response.json()['content'][1]['name']) is str
    #  c. isHardSkill — Boolean
    assert type(response.json()['content'][2]['isHardSkill']) is bool
    #  d. skillIds — Array
    assert type(response.json()['content'][2]['skillIds']) is list

#  4. Тест, что json содержит объект pageable
    assert 'pageable' in response.json()

#  5. Тест, что нижеописанные поля присутствуют в объекте pageable и соответствуют типам
    #  a. pageSize – Number
    assert type(response.json()['pageable']['pageSize']) is int
    #  b. pageNumber – Number
    assert type(response.json()['pageable']['pageNumber']) is int
    #  c. offset – Number
    assert type(response.json()['pageable']['offset']) is int
    #  d. unpaged – Boolean
    assert type(response.json()['pageable']['unpaged']) is bool
    #  e. paged – Boolean
    assert type(response.json()['pageable']['paged']) is bool

#  6. Тест, что в объекте pageable присутствует подобъект sort
    assert 'sort' in response.json()['pageable']

#  7. Тест, что объект sort содержит нижеописанные поля и данные поля соответствуют типам: 
    #  a. sorted – Boolean
    assert type(response.json()['pageable']['sort']['sorted']) is bool
    #  d. unsorted – Boolean
    assert type(response.json()['pageable']['sort']['unsorted']) is bool
    #  e. empty – Boolean
    assert type(response.json()['pageable']['sort']['empty']) is bool

