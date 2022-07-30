set all [atomselect top all]
#set screen [atomselect top "(segname MEMB) or (segname PROA PROC PROE and resid 0 to 405) or (same residue as resname TIP3 and within 10 of segname MEMB and not sqr(z)<500)"]
measure sasa 1.0 $all -points sasapoints
set outfile [open pts_mem.txt w]

foreach pt $sasapoints {
        draw point $pt
        puts $outfile "$pt"
}
$all delete

