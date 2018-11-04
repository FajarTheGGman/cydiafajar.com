#!/usr/bin/python
"""
#####################################
# Auxscan Project                   #
# MyFB : www.fb.com/100004136748473 #
#####################################
# Author: DedSecTL                  #
# BlackHoleSec Dev                  #
#####################################
"""
"""
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import os
import sys
import time
from core.misc import *
from core.axscn import *

def main():
	clearscreen()
	banner()
	menu()
	auxscan = raw_input("[*] Auxscan > ")
	
	if auxscan.strip() in '01 1'.split():
		apf()
	elif auxscan == '02' or auxscan == '2':
		goodork()
	elif auxscan == '03' or auxscan == '3':
		whs()
	elif auxscan == '04' or auxscan == '4':
		portx()
	elif auxscan == '05' or auxscan == '5':
		rc()
	elif auxscan == '06' or auxscan == '6':
		prc()
	elif auxscan == '07' or auxscan == '7':
		upf()
	elif auxscan == '08' or auxscan == '8':
		trcrt()
	elif auxscan == '09' or auxscan == '9':
		dnslkp()
	elif auxscan == '10':
		geoip()
	elif auxscan == '11':
		httphg()
	elif auxscan == '00' or auxscan == '0':
		sys.exit()
	else:
		print "\n[!] Wrong input"
		time.sleep(2)
		restart_program()

if __name__ == "__main__":
	main()