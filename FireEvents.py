import datetime


class FireEvents():

    fire_event_script = "function fireEvent(element, event) {if (document.createEventObject) {var evt = document.createEventObject();return element.fireEvent('on'+event, evt);} else {var evt = document.createEvent('HTMLEvents');evt.initEvent(event, true, true);return !element.dispatchEvent(evt);}};"
    data = {
        "%1$@": "Abc",
        "%2$@": "If",
        "%3$@": "Xyz",
        "%26$@": "abcdef",
        "%33$@": "abc123",
        "%27$@": "LAS",
        "%32$@": "LAS",
        "%34$@": "AA",
        "%35$@": "55",
        "%11$@": "abc@xyz.com",
        "%38$@": str(int(datetime.datetime.now().strftime("%m"))),
        # A little hack to trim the starting zero, feel free to refactor
        "%39$@": str(int(datetime.datetime.now().strftime("%d")) + 1),
        "%40$@": str(int(datetime.datetime.now().strftime("%Y"))),
        "%8$@": "123",
        "%9$@": "456",
        "%10$@": "7890",
        "%28$@": "1"
    }