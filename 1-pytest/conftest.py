from pytest import fixture

@fixture(params = [(2,3,6), (4,5,20)])
def multiply_data(request):
    return request.param