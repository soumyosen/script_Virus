
set residues [lsort -unique [[atomselect top "segname MEMB"] get residue]]
set f [open "lipid_pts.csv" w]

foreach res $residues {
	set atom [measure center [atomselect top "residue $res and (type PL or type OHL)"]]
	set x [lindex $atom 0]
	set y [lindex $atom 1]
	puts $f "$res,$x,$y"
}



