from fetch_verify_code import FetchVerifyCode

a = FetchVerifyCode(src_url='https://yunduanxin.net/code/5U086d1wHUWfoXdk50c-2')
a.b64_img = a.im_2_b64()

print(a.get_code())
