
import "task.wdl" as lib

workflow test_task{
    File read1
    File read2


    call lib.megahit as megahit {
        input:
            read1=read1,read2=read2
    }

}




