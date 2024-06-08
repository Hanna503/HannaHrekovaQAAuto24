import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    assert len(orders) == 1
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


@pytest.mark.database
def test_add_unsupported_data_type(db):
    db = Database()
    with pytest.raises(ValueError, match="Unsupported data type"):
        db.add_data(set([1, 2, 3]))


@pytest.mark.database
def test_update_data_out_of_range():
    db = Database()
    with pytest.raises(ValueError, match="Unsupported data type"):
        db.update_data(10, set([1, 2, 3]))


@pytest.mark.database
def test_add_large_values():
    db = Database()
    large_value = "a" * 100
    assert db.add_large_values(large_value)
    data = db.get_data()
    assert len(data) == 1
    assert data[0][1] == large_value


@pytest.mark.database
def test_add_unsupported_type():
    db = Database()
    with pytest.raises(ValueError) as excinfo:
        db.add_data(set([1, 2, 3]))
    assert "Unsupported data type" in str(excinfo.value)


@pytest.mark.database
def test_get_data_by_id():
    db = Database()
    db.add_data("test_value")
    data = db.get_data()
    data_id = data[0][0]
    retrieved_data = db.get_data_by_id(data_id)
    assert retrieved_data is not None


@pytest.mark.database
def test_delete_all_data():
    db = Database()
    db.add_data("data1")
    db.add_data("data2")
    db.clear_table()
    data = db.get_data()
    assert len(data) == 0