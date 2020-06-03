from drivennav.brands import facade


def list_brands(request):
    return {"BRANDS": facade.list_brands_ordeneds()}
