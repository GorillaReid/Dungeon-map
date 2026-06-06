import random
import threading

timeout = 5
s = 0

def timed_input(prompt, timeout=5):
	result = [None]

	def get_user_input():
		try:
			result[0] = input(prompt)
		except:
			result[0] = None

	thread = threading.Thread(target=get_user_input)
	thread.daemon = True
	thread.start()
	thread.join(timeout)

	if thread.is_alive():
		print("\nTime's up!")
		return None
	return result[0]

while timeout > 0:
	a = random.randint(1,9)
	b = random.randint(1,9)

	ans = timed_input(f"{a}+{b}=")

	if ans is None:
		break
	try:
		x = int(ans)
		if x == a+b:
			s += 1
	except ValueError:
		print("Invalid chacter, try again")

print("score", s)
