#set f [open "lipid_num_dens.csv" w]

for {set i 0} {$i < 100} {incr i} {
	set lowerbound [expr $i-30]
	set upperbound [expr $lowerbound + 1]
	set sel [atomselect top "not protein and z>$lowerbound and z<$upperbound"]
	set selnum [$sel num]
	set cent [expr [expr $lowerbound+$upperbound]/2.0]
	puts "$cent $selnum"
}

 
