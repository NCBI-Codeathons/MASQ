
import "task.wdl" as lib

workflow test_task{
     File bam_file
     File bam_file_index
     File ref_file
     File ref_file_index

    call lib.manta as manta {
        input:
          bam_file=bam_file,bam_file_index=bam_file_index,ref_file=ref_file,ref_file_index=ref_file_index
    }

}




