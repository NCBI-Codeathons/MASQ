task manta {

     File bam_file
     File bam_file_index
     File ref_file
     File ref_file_index
    command {

        python /usr/local/bin/configManta.py --bam ${bam_file} --referenceFasta ${ref_file} --runDir manta_rep0
        python ./manta_rep0/runWorkflow.py -m local -j 16

    }

    output {
       File diploidSV="./manta_rep0/results/variants/diploidSV.vcf.gz"
       File candidateSV="./manta_rep0/results/variants/candidateSV.vcf.gz"
       File candidateSmallIndels="./manta_rep0/results/variants/candidateSmallIndels.vcf.gz"
       File alignmentStats="./manta_rep0/results/stats/alignmentStatsSummary.txt"
    }

    runtime{
        docker: "quay.io/biocontainers/manta:1.6.0--py27_0"
        dx_instance_type: "azure:mem1_ssd1_x16"
    }
}