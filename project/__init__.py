def translate(english_word):
    dict ={
        'hello': 'namaskar', 'good morning': 'suvah bihani'
    }
    try:
        return dict[english_word.lower()]
    except  Exception as e:
        return "not in dictionary"