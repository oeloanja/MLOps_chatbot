import screening_input


path = "C:/Users/user/Downloads/test4.pdf"
msg = "여기서 입사연월을 알려줘"
result = screening_input.get_data(path, msg)
print(result)