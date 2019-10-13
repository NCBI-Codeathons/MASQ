All relevant parameters are discussed here.

## BWA:
```
bwa mem -t 16 -K 100000000 -Y -R @RG\tID:BioPool_BioPool_Cycle_02042016_CTGAAGCT-TATAGCCT_L001_001_2\tPL:ILLUMINA\tPU:BioPool_BioPool_Cycle_02042016_CTGAAGCT-TATAGCCT_L001_001_2\tLB:SRR606249\tSM:SRR606249 genome/zymoSpadesAssembly.fa /home/dnanexus/in/reads_fastqgzs/1/BioPool_BioPool_1_Cycle_02042016_CTGAAGCT-TATAGCCT_L001_R1_001.fastq.gz /home/dnanexus/in/reads2_fastqgzs/1/BioPool_BioPool_1_Cycle_02042016_CTGAAGCT-TATAGCCT_L001_R2_001.fastq.gz
```
## Manta:
```
       python /usr/local/bin/configManta.py --bam ${bam_file} --referenceFasta ${ref_file} --runDir manta_rep0
        python ./manta_rep0/runWorkflow.py -m local -j 16
```
## Sniffles:
```
./sniffles -m <bam file> -v <out.vcf>  -l 10 
```

```
Estimating parameter...
    Max dist between aln events: 5
    Max diff in window: 50
    Min score ratio: 2
    Avg DEL ratio: 0.0592809
    Avg INS ratio: 0.0395852
```
## Minimap2:
```
docker run -v /home/dnanexus:/home/dnanexus -w /home/dnanexus quay.io/biocontainers/minimap2:2.14--ha92aebf_0 minimap2 -ax map-pb fixed.mmi ZymoGridIONLOGBBSN.fq.gz 
```
## Truvari:
```
{
    "base": "../fixed_sniffles.vcf.gz",
    "comp": "../zymo_log/fixed_sniffles.vcf.gz",
    "output": "even_log_truvari",
    "reference": null,
    "giabreport": false,
    "debug": false,
    "prog": false,
    "refdist": 500,
    "pctsim": 0.0,
    "pctsize": 0.7,
    "pctovl": 0.0,
    "typeignore": false,
    "gtcomp": false,
    "bSample": null,
    "cSample": null,
    "sizemin": 0,
    "sizefilt": 0,
    "sizemax": 50000,
    "passonly": false,
    "no_ref": false,
    "includebed": null,
    "multimatch": false
}
```
