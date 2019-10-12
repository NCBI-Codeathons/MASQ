task megahit {

    File read1
    File read2
    command {

        megahit -1 ${read1} -2 ${read2} -t $(nproc) -o out

    }

    output {
       File assemble="out/final.contigs.fa"
    }

    runtime{
        docker: "vout/megahit"
        dx_instance_type: "azure:mem1_ssd1_x16"
    }
}