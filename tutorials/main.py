

def templates():
	'''
		Learning Templates
		------------------
		Templates provide an easy way to print out large formatted texts
	'''
	from string import Template
	cart = [
		dict(name="Pepsi", qty=10, price=4.0),
		dict(name="Coke", qty=20, price=2.0)
	]

	template = Template("$name: $qty x $price")
	for product in cart:
		print template.substitute(product) + ': $%.2f' % (product['qty'] * product['price'])



def rsum(inlist):
	if not inlist:
		return None
	res = 0
	for item in inlist:
		if type(item) == type([]):
			res += rsum(item)
		else:
			res += item
	return res

def recursion1():
	'''
		Learning Recursion
		------------------
		Question: Find sum elements in nested lists
	'''
	inlist = [ 1,2,[5,7,[10,2,3],12,1],[10,2]]
	result = rsum(inlist)
	print result



def rmax(inlist):
	result = None
	for item in inlist:
		if type(item) == type([]):
			result = max(result, rmax(item))
		else:
			result = max(result, item)

	return result

def recursion2():
	'''
		Learning Recursion
		------------------
		Question: Find max element in nested lists
	'''
	inlist = [ 1,2,[5,7,[10,2,3],12,1],[10,2]]
	result = rmax(inlist)
	print result




def regex1():
	'''
		Learning Regex
		------------------
		re.match for IP addresses

	'''
	import re
	ips = ["1.2.3.4", '255.255.255.0', '833.122.132.432', '122,122.1,32']

	num_pattern = r'[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]'
	pattern = r'^({0})\.({0})\.({0})\.({0})$'.format(num_pattern)
	ip_regex = re.compile(pattern)

	for ip in ips:
		match = ip_regex.match(ip)
		if match:
			print match.group() + ": IS a valid IP"
		else:
			print ip + ": is NOT a valid IP"


def regex2():
	'''
		Learning Regex
		------------------
		Search for words in a line
	'''
	import re
	line = "Hey Harshit ! Hows it going buddy ??"

	# NOTE: case sensitive
	matchcase = re.search("Harshit", line)
	if matchcase:
		print matchcase.group(), "Matched:", "Harshit"
	else:
		print "No match for Harshit."

	# NOTE: Ignore case match
	match = re.search('harshit', line, re.IGNORECASE)
	if match:
		print matchcase.group(), "Matched: ", 'harshit'
	else:
		print "No match for harshit"


def regex3():
	'''
		Learning Regex
		------------------
		re.match vs re.search
	'''
	import re
	line = "Hey Harshit ! Hows it going buddy ??"

	# NOTE: re.match looks for an exact match
	match = re.match('Harshit', line)
	if match:
		print "Harshit IS " + line
	else:
		print "Harshit IS NOT " + line

	search = re.search('Harshit', line)
	if search:
		print "Harshit IS IN " + line
	else:
		print "Harshit IS NOT IN " + line


def timer(name, delay, repeat):
	from time import sleep
	for i in xrange(repeat):
		print name + " has fired"
		sleep(delay)

def threads1():
	'''
		Learning Threads
		------------------
		Basic syntax for using Threads.
	'''
	from threading import Thread

	# NOTE: Specify target & args
	t1 = Thread(target=timer, args=("Thread1", 0.2, 4))
	t2 = Thread(target=timer, args=("Thread2", 0.1, 4))

	# Start running the thread
	t1.start()
	t2.start()


from threading import Lock
t_lock = Lock()

def sync_timer(name, delay, repeat):
	from time import sleep

	t_lock.acquire()
	print name, "has acquired the lock"

	# NOTE: The below for loop is critical region code
	for i in xrange(repeat):
		print name + " has fired"
		sleep(delay)

	t_lock.release()
	print name, "has released the lock"


def threads2():
	'''
		Learning Threads
		------------------
		Lock acquire & release against
	'''
	from threading import Thread

	t1 = Thread(target=sync_timer, args=("Thread1", 0.2, 4))
	t2 = Thread(target=sync_timer, args=("Thread2", 0.1, 4))

	t1.start()
	t2.start()

	print "Main has finished - the threads could still be running"


def threads3():
	'''
		Learning Threads
		------------------
		Thread Joins - Wait until the thread terminates. This blocks the calling thread until
		the thread whose join() method is called terminates - either normally or
		though an unhandled exception - or until the optional timeout occurs.
	'''
	from threading import Thread

	t1 = Thread(target=timer, args=("Thread1", 1, 4))
	t2 = Thread(target=timer, args=("Thread2", 0.1, 4))
	t1.start()
	t1.join()

	# NOTE: This part runs only after thread1 is done executing
	t2.start()
	t2.join()

	# NOTE: This part runs only after thread1 & thread2 is done executing
	print "Main has finished - the threads could still be running"


def make_bold(func):
	from functools import wraps
	@wraps(func)
	def func_wrapper(name):
		return '<strong>'+func(name)+'</strong>'
	return func_wrapper

@make_bold
def greet1(name):
	return "Hello: " + name + ". How are you doing ?"

def decorators1():
	'''
		Learning Decorators
		------------------
		Simple decorator
	'''
	print greet1("Harshit")


def add_tag(tag):
	from functools import wraps
	def dec(func):
		@wraps(func)
		def func_wrapper(name):
			return '<'+tag+'>' + func(name) + '</'+tag+'>'
		return func_wrapper
	return dec

@add_tag("strong") # 2nd wrapper: <strong><h1>Harshit</h1><strong>
@add_tag("h1") # 1st wrapper: <h1>Harshit</h1>
def greet2(name):
	return "Hello: " + name + ". How are you doing ?"

def decorators2():
	'''
		Learning Decorators
		------------------
		Decorators accepting arguments
	'''
	print greet2("Harshit")


def ask_question(func):
	from functools import wraps
	@wraps(func)
	def func_wrapper(name):
		return func(name) + " Hope your doing great ??"
	return func_wrapper

@ask_question
@make_bold
def greet3(name):
	return "Hello: " + name + "."

def decorators3():
	'''
		Learning Decorators
		------------------
		Multiple Decorators decorating a single function
	'''
	print greet3("Harshit")


def gen_data():
	yield 1
	yield 2
	yield 3

def generators1():
	'''
		Learning Generators
		------------------
		Simple Generator yielding 3 values
	'''
	gen = gen_data()
	print next(gen)
	print  next(gen)
	print next(gen)
	try:
		print next(gen)
	except StopIteration:
		print "Hit StopIteration exception !!"

	gen = gen_data()
	for i in gen:
		print i

def is_even(i):
	if i%2:
		return False
	return True

def even_genfunc(start, end):
	for i in xrange(start, end+1):
		if is_even(i):
			yield i

def generators2():
	'''
		Learning Generators
		------------------
		A practical example of generators with a real example - generate even numbers
	'''
	even_list = []
	even_gen = even_genfunc(start=0, end=100)
	for i in even_gen:
		even_list.append(i)
	print ",".join(map(str, even_list))



class Counter(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end
	def __iter__(self):
		start = self.start
		for i in xrange(start, self.end+1):
			if i%2 == 0:
				yield i

def generators3():
	'''
		Learning Generators
		------------------
		Reusable Generators - using Object based generators - eg: generate even numbers
	'''
	counter = Counter(start=0, end=100)
	evens = []
	for c in counter:
		evens.append(c)
	print ','.join(map(str, evens))



def consume():
	items_seen = 0
	running_sum = 0
	while(True):
		data = yield
		items_seen += len(data)
		running_sum += sum(data)
		print "The running sum is {}".format(running_sum/float(items_seen))

def produce(limit, consumer):
	from random import sample
	for i in range(limit):
		randlist = sample(range(10), 3)
		consumer.send(randlist)
		yield randlist

def generators4():
	'''
		Learning Generators
		------------------
		Producer/Consumer - using send() method
	'''
	consumer = consume()
	consumer.send(None)
	producer = produce(10, consumer)
	for randlist in producer:
		print "Producer produced: {}".format(randlist)


def main():
	'''
	print " === Templates === "
	templates()

	print " === Recursion 1 === "
	recursion1()

	print " === Recursion 2 ==="
	recursion2()

	print " === Regex 1 ==="
	regex1()

	print " === Regex 2 ==="
	regex2()

	print " === Regex 3 ==="
	regex3()

	print " === Threads 1 ==="
	threads1()
	
	print " === Threads 2 ==="
	threads2()

	print " === Threads 3 ==="
	threads3()

	print " === Decorators 1 ==="
	decorators1()
	
	print " === Decorators 2 === "
	decorators2()
	
	print " === Decorators 3 ==="
	decorators3()

	print " === Simple Generators ==="
	generators1()
	
	print " === Real Generator Example ==="
	generators2()

	print " === Reusable Generator === "
	generators3()
	'''
	print " === Producer/Consumer - using send() === "
	generators4()

if __name__ == "__main__":
	main()