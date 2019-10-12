task sniffles {

    File mapped_reads
    File mapped_reads_index

    String output_prefix=basename(mapped_reads, ".bam")

    String? advanced_options

    command {

        sniffles -m ${mapped_reads} -v ${output_prefix}.vcf ${advanced_options}

    }

    output {
        File vcf = "${output_prefix}.vcf"
    }

    runtime{
        docker: "quay.io/biocontainers/sniffles:1.0.11--hdbcaa40_1"
        dx_instance_type: "azure:mem1_ssd1_x16"
    }
}