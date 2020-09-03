import os
import time
import threading

def change_default_browser():
	PATH = r'C:\MBG\SetDefaultBrowser\SetDefaultBrowser.exe'
	EXPLORER = r'HKLM Brave'
	# EXPLORER = r'chrome'
	os.system('{} {}'.format(PATH, EXPLORER))

def open_timetable():
	# Open Timetable Excel
	os.system(r'C:\MBG\Google_Drive\Timetable.xlsx')
	

if __name__ == '__main__':
	t = threading.Thread(target=change_default_browser, name='Change default browser')
	t.daemon = True
	print('Changing default browser to Brave...')
	t.start()
	time.sleep(1)

	t = threading.Thread(target=open_timetable, name='Open Timetable')
	t.daemon = True
	print('Opening Timetable...')
	t.start()
	time.sleep(1)