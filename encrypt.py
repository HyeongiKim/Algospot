def encrypt(sen):
	i=0;
	sen_1 = "";
	sen_2 = "";

	sen_len = len(sen);
	for i in range(sen_len):
		if (i%2):
			sen_2 += sen[i];
		else:
			sen_1 += sen[i];

	return sen_1 + sen_2;

	
def main():
	i = 0;
	num = input();

	for i in range(num):
		temp = raw_input();
		print(encrypt(temp));
	return;

main();
