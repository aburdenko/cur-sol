defunct(){
	    echo "Children:"
	        ps -ef | head -n1
		    ps -ef | grep defunct
		        echo "------------------------------"
			    echo "Parents:"
			        ppids="$(ps -ef | grep defunct | awk '{ print $3 }')"
				    echo "$ppids" | while read ppid; do
				            ps -A | grep "$ppid"
					        done
					}
