from drivennav.channel import facade


def list_brands(request):
    return {"CHANNELS": facade.list_channels_ordeneds()}
