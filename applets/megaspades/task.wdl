task megaspades {

    File read1
    File read2
    command {

        python /usr/metaspades/SPAdes-3.11.1-Linux/bin/metaspades.py -1 ${read1} -2 ${read2} -o out --threads $(nproc)

    }

    output {
       File assemble="out/contigs.fasta"
    }

    runtime{
        docker: "quay.io/fhcrc-microbiome/metaspades:latest"
        dx_instance_type: "azure:mem1_ssd1_x16"
    }
}