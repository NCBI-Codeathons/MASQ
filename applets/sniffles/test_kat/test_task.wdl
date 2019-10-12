
import "task.wdl" as lib

workflow test_task {
    File mapped_reads
    File mapped_reads_index

    String output_prefix=basename(mapped_reads, ".bam")

    String? advanced_options

    call lib.sniffles as sniffles {
        input:
          mapped_reads=mapped_reads,mapped_reads_index=mapped_reads_index,advanced_options=advanced_options
    }

}




