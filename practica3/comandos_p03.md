# Comandos de la Práctica 01
**Kevin Axel Prestegui Ramos**

## Parte I. 

**Respuesta 1:** Creación de directorios y archivos.
Comandos: 

```console
% cd Desktop
% mkdir GenomicaComputacional
% mkdir kprestegui_p03
% touch comandos_p03.md
```


**Respuesta 2:** Tipo de shell.
Comando:

```console
% echo $0
```

Output:
```console
/bin/zsh
```


**Respuesta 3:** Creación de directorios para proyecto bioinformático.

Comandos:
```console
mkdir -p data/filtered data/raw_data meta scripts figures archive
```

**Respuesta 4:**

Como se explica en la página, todo proyecto bioinformático (y en general, todo proyecto) debe de estar estructurado, organizado y bien documentado, de forma que cualquier persona que desea reproducirlo, tenga todo lo necesario para hacerlo.

En un proyecto bioinformático lo usual será que tenga su propio directorio, el cual contendrá más directorios para la organización de todos sus elementos. Se recomienda:

1. **data**, contiene los datos. Estos datos pueden a su vez dividirse en *raw*, *filtered*, *genotypes*, etc, todos con sus directorios dentro de **data**.
2. **meta** (o también **info** o **docs**), contiene los metadatos. 
3. **scripts**(o **bin**), contiene todos los scripts necesarios para realizar la ejecución del programa (el análisis).
4. **figures**, contiene código utilizado para graficar y realizar distintas figuras que se usan en la publicación.
5. **archive**, contiene scripts y resultados que se cree no se necesitarán más, pero que siempre es seguro tener respaldados y no borrarlos por completo.

## Parte II.
**Respuesta 1:**
Entramos a *scripts* y creamos un archivo *delay.sh* con lo solicitado en la práctica 

Comandos:

```console
% cd scripts/
% cat > delay.sh

#!/bin/bash
echo "Después de la Parte I. necesito un descanso de exactamente 30 segundos."
```

**Respuesta 2:**

Damos permisos de ejecución.

Comandos:

```console
% chmod u=xrw,g=r,o=r delay.sh
```

**Respuesta 3:**

Verificamos que se tiene permiso para ejecutar, y lo ejecutamos.

Comandos:

```console
% ls -@l delay.sh
% ./delay.sh
Después de la Parte I. necesito un descanso de exactamente 30 segundos.
```

**Respuesta 4:**
Agregamos el comando para dormir por 30 segundos ```sleep 30``` a *delay.sh*, lo ejecutamos.

```console
% ./delay.sh
Después de la Parte I. necesito un descanso de exactamente 30 segundos.
Ya puedo continuar!
```

**Respuesta 5:**
Se modifica el comando ```sleep 30``` por ```sleep 300```. Lo ejecutamos y matamos:

```console
% ./delay.hs &
% ps
 PID TTY           TIME CMD
 2771 ttys001    0:00.21 /bin/zsh -l
 4293 ttys001    0:00.00 /bin/bash ./delay.sh
% kill -9 4293
```

## Parte III.
Movemos los archivos al directorio **data\raw_data**.
```console
% cd Downloads
% mv sarscov2_genome.* splike_*.fasta SRR10971381_R*.* contigs.fasta /Users/axelpresteguiramos/Desktop/GenomicaComputacional/kprestegui_p03/data/raw_data 
```
Cambie el nombre de **sarscov2_assembly.fasta.gz** a **contigs.fasta**, pues al descargarlo se me descomprimía con ese nombre de manera inmediata.

## Parte IV.
**Respuesta 1:**

Creamos las ligas simbólicas:
```console
% ln -s /Users/axelpresteguiramos/Desktop/GenomicaComputacional/kprestegui_p03/data/raw_data/splike_a.fasta  /Users/axelpresteguiramos/Desktop/GenomicaComputacional/kprestegui_p03/data/filtered
% ln -s /Users/axelpresteguiramos/Desktop/GenomicaComputacional/kprestegui_p03/data/raw_data/splike_a.fasta  /Users/axelpresteguiramos/Desktop/GenomicaComputacional/kprestegui_p03/data/filtered
% ln -s /Users/axelpresteguiramos/Desktop/GenomicaComputacional/kprestegui_p03/data/raw_data/splike_c.fasta  /Users/axelpresteguiramos/Desktop/GenomicaComputacional/kprestegui_p03/data/filtered
```

**Respuesta 2:**

Nos movemos a **data/filtered** y creamos el archivo **glycoproteins.faa**:

```console
% cd data/filtered
% touch glycoproteins.faa
```

**Respuesta 3:**

Obtenemos las primeras lineas de **splike_*.faa**
```console
% head -1 splike_*.fasta
==> splike_a.fasta <==
>pdb|6VXX|A Chain A, Spike glycoprotein

==> splike_b.fasta <==
>pdb|6VXX|B Chain B, Spike glycoprotein

==> splike_c.fasta <==
>pdb|6VXX|C Chain C, Spike glycoprotein
```

**Respuesta 4:**

Redireccionamos el contenido de los archivos **splike_*.faa** al archivo **glycoproteins.faa** en orden a,b y c:

```
% cat splike_a.fasta splike_b.fasta splike_c.fasta > glycoproteins.faa
```

**Respuesta 5:**

Movemos los archivos **splike_*.faa** a **archive**:
```
% mv splike_*.fasta /Users/axelpresteguiramos/Desktop/GenomicaComputacional/kprestegui_p03/archive
```

Las ligas suaves dejaron de servir :c

**Respuesta 6:**

Imprimimos las primeras 3 líneas de los archivos **sarscov2_genome.fasta** y **sarscov2_assembly.fasta.gz** (en mi caso **contigs.fasta**)

```console
% head -3 sarscov2_genome.fasta contigs.fasta 
==> sarscov2_genome.fasta <==
>NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA
CGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAAC

==> contigs.fasta <==
>NODE_1_length_264_cov_161.042781
CACAAATCTTAACACTCTTCCCTACACGACGCTCTTCCGATCTACGCCGGGCCATTCGTA
CGAACCGATACCTGTGGTAAAGGGTCCTACTGTATGGTGGTACACGAGTAGTAGCAAATG
```

**Respuesta 7:**

Para cada archivo, contamos el número de >:

```console
% grep -o '>' contigs.fasta | wc -l
      35
% grep -o '>' sarscov2_genome.fasta | wc -l
      1
```

**Respuesta 8:**

Obtenemos las primeras 12 líneas de **SRR10971381_R2.fastq**:

```console
% head -12  SRR10971381_R2.fastq
@SRR10971381.512_2
CGTGGAGTATGGCTACATACTACTTATTTGATGAGTCTGGTGAGTTTAAAGTGGCTTCACATATGTATTGTTCTTTCTACCCTCCAGATGAGGATGAAGAAGAAGGTGATTGTGAAGAAGAAGAGTTTGAGCCATCAACTCAATATGAGT
+
/FFFA/A/FFFF66FFFFFF/FF/FFFFFFFFFFFFF/AFFF6FFFA6FFFFF/FFFFFFFFFFFFFFFFFF/FF/FFFFFA/FFF/FFF/A/AFA/FFFFF/=F/F/F/AFAFF//A/AFF//FFAF/FFF=FFAFFFA/A/6=///==
@SRR10971381.556_2
TTTGTAAAAATAAAATAAAAAAAATAAAAATAATATATTAAAAAAAGATAAATAAAAAAATGAACAATTAATAAAAAAAAAAAAAAAAAAAAATTAAAAAAAAAAAAAAAAAAAATAAAAAAAAAAAAAAATAAAAAAAAAATTATAAAA
+
6AFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF/FFFAFFFFFF/FFA/FF=F//=FF/FFFFFFFFFFFFFA/FFFF/FF/FA//F/FFFFFFA/=FFFFF/FFFF/F=FFFAFF///FFFFA/FF/6//////=/
@SRR10971381.1428_2
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
+
FFFFFFFFFFFFAFFFAFFFFFF6A//F//FFF
```

Creo que podríamos usar **@** para poder obtener el conteo de secuencias en el archivo:

```console
% grep -o '@' SRR10971381_R2.fastq | wc -l
  130022
```

**Respuesta 9:**

Los archivos .fasta son un formato para secuencias de DNA para representar y especificar secuencias de este. Los archivos .fastaq resuleven un gran problema, y es que entre todas las tecnologías para secuencias, la probabilidad de que una secuenciación sea correcta varía. Eso se expresa en el [Phred quality score](https://en.wikipedia.org/wiki/Phred_quality_score).
El NCBI utiliza los archivos .faa para los aminoácidos FASTA, lo que significa que se trata de un archivo de proteínas. En general, los .fasta pueden usar para representar secuencias de ácidos nucléicos o para aminoácidos.

**Respuesta 10:**

No estoy seguro si por **less sequence.gff3** se referían al archivo **sarscov2_genome.gff3**, porque solo tengo ese archivo con extensión gff3 :c

Al correr **less sarscov2_genome.gff3** lo que imprimía estaba en extremo desordenado y no era legible para su lectora. Usar la bandera -S hace que se imprima de manera ordenada y muy legible.

**Respuesta 11:**
Contamos el número de veces que **gene** aparece en la tercer columna:
```console
% awk '($3 == "gene") {count++ } END { print count }' sarscov2_genome.gff3 
11
```
El campo tres corresponde al tipo del campo que va a ser tomado de un vocabulario,
es decir, se debe de escoger de algún conjunto de tipos que ya están predeterminados.
Esto está limitado a ser un término de Sequence Ontology o un número de acceso SO.
**gene** denota una región completa de DNA que es responsable de todos su RNA producido. CDS
comprende solamente la región que codifica la proteína.

## Parte V

**Respuesta 1:**

Creamos la liga simbólica:

```console
figures % ln -s /Users/axelpresteguiramos/Desktop/GenomicaComputacional/kprestegui_p03/data/raw_data/sarscov2_genome.gff3
```

**Respuesta 2:**

Identificamos las distintas categorías en el campo 3, y cuántas aparecen. Redireccionamos la salida
a barplot_data.txt
```console
figures % sed 1,2d sarscov2_genome.gff3 | awk '                        
  {a[$3]}
  {
    for(i=1; i<=NF; i++){
      if ($i in a){ a[$i]++ }
    }
  }
  END{
    for(key in a){ printf "%s %d\n", key, a[key] }
  }
' > barplot_data.txt
```
Primero eliminamos los headers del documento y el resultado se lo pasamos a awk para que encuentre
las categorías y las cuente.

**Respuesta 3: **
Nos quedamos solo con las categorías:
```console
% awk '!($2="")' barplot_data.txt > tmp && mv -f tmp barplot_data.txt
```

**Respuesta 4:**

Volvemos a obtener los datos completos para poder graficarlos:
```console
figures % sed 1,2d sarscov2_genome.gff3 | awk '                        
  {a[$3]}
  {
    for(i=1; i<=NF; i++){
      if ($i in a){ a[$i]++ }
    }
  }
  END{
    for(key in a){ printf "%s %d\n", key, a[key] }
  }
' > barplot_data.txt
```