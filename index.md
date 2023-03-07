# Table of contents
{:.no_toc}
* toc
{:toc}

# Abstract
<img src="figure1.png" width="100%">

This paper presents FastFit, a novel neural vocoder architecture that replaces U-Net's encoder with multiple short-time Fourier transforms (STFTs) to achieve faster generation rates without sacrificing sample quality. We replace each encoder block with an STFT, with parameters equal to the temporal resolution of each decoder block leading to the skip-connection. FastFit reduces the number of parameters and generation time of the model by almost half while maintaining high fidelity. Through objective and subjective evaluations, we demonstrate that the proposed model achieves nearly twice the generation speed of the baseline iteration-based vocoders while maintaining high sound quality. We also show that FastFit produces similar sound quality to other baselines in text-to-speech evaluation scenarios, including multi-speaker and zero-shot text-to-speech.

# Comparison with baselines
* We adopted [LibriTTS](https://openslr.org/60/), a multi-speaker English dataset which has 24 kHz sampling rate waveforms.
* For training models, a 'train-clean-360' dataset was used.
* For ground-truth mel-spectrogram evaluation (GT mel evaluation) including the ablation study, a 'test-clean' dataset was prepared.

## Application to text-to-speech synthesis
* For multi-speaker TTS, we trained the [JDI-T](https://arxiv.org/abs/2005.07799) acoustic model using the LibriTTS 'train-clean-360' subset with 100 speakers.
* For zero-shot TTS evaluation, we used an open-source TTS program named [TorToiSe](https://github.com/neonbjb/tortoise-tts).
  - The recordings of the LibriTTS ’test-clean’ subset with 10 speakers were input into the program with an 'ultra-fast' offset.
* Each vocoder was not fine-tuned with these predicted mel-spectrograms.

### Multi-speaker text-to-speech
<table>
    <thead>
        <th>Models</th>
        <th>#1</th>
        <th>#2</th>
        <th>#3</th>
        <th>#4</th>
    </thead>
    <tbody>
        <tr>
            <th>UnivNet</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/univnet/100_121669_10.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/univnet/114_129324_15.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/univnet/176_123271_26.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/univnet/1027_125410_50.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>FastDiff</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/fastdiff/100_121669_10.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/fastdiff/114_129324_15.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/fastdiff/176_123271_26.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/fastdiff/1027_125410_50.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>WaveFit</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/wavefit/100_121669_10.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/wavefit/114_129324_15.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/wavefit/176_123271_26.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/wavefit/1027_125410_50.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>FastFit</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/proposed/100_121669_10.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/proposed/114_129324_15.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/proposed/176_123271_26.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/proposed/1027_125410_50.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>FastFit (U-Net)</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/u-net/100_121669_10.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/u-net/114_129324_15.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/u-net/176_123271_26.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/multispk/u-net/1027_125410_50.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
</table>

### Zero-shot text-to-speech
<table>
    <thead>
        <th>Models</th>
        <th>#1</th>
        <th>#2</th>
        <th>#3</th>
        <th>#4</th>
    </thead>
    <tbody>
        <tr>
            <th>UnivNet</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/univnet/10.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/univnet/15.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/univnet/26.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/univnet/50.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>FastDiff</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/fastdiff/10.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/fastdiff/15.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/fastdiff/26.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/fastdiff/50.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>WaveFit</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/fastdiff/10.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/fastdiff/15.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/fastdiff/26.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/fastdiff/50.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>FastFit</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/proposed/10.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/proposed/15.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/proposed/26.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/proposed/50.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>FastFit (U-Net)</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/u-net/10.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/u-net/15.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/u-net/26.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/zeroshot/u-net/50.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
</table>

## Ground truth mel-spectrogram
<table>
    <thead>
        <th>Models</th>
        <th>#1</th>
        <th>#2</th>
        <th>#3</th>
        <th>#4</th>
    </thead>
    <tbody>
        <tr>
            <th>Recordings</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/recordings/1089_134686_000002_000000.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/recordings/2300_131720_000002_000001.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/recordings/3570_5694_000005_000003.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/recordings/4446_2275_000001_000000.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>UnivNet</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/univnet/1089_134686_000002_000000.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/univnet/2300_131720_000002_000001.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/univnet/3570_5694_000005_000003.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/univnet/4446_2275_000001_000000.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>FastDiff</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/fastdiff/1089_134686_000002_000000.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/fastdiff/2300_131720_000002_000001.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/fastdiff/3570_5694_000005_000003.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/fastdiff/4446_2275_000001_000000.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>WaveFit</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/wavefit/1089_134686_000002_000000.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/wavefit/2300_131720_000002_000001.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/wavefit/3570_5694_000005_000003.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/wavefit/4446_2275_000001_000000.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>FastFit</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/proposed/1089_134686_000002_000000.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/proposed/2300_131720_000002_000001.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/proposed/3570_5694_000005_000003.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/proposed/4446_2275_000001_000000.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>FastFit (U-Net)</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/u-net/1089_134686_000002_000000.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/u-net/2300_131720_000002_000001.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/u-net/3570_5694_000005_000003.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/gt-evaluation/u-net/4446_2275_000001_000000.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
</table>

# Ablation studies
<table>
    <thead>
        <th>Models</th>
        <th>#1</th>
        <th>#2</th>
        <th>#3</th>
        <th>#4</th>
    </thead>
    <tbody>
        <tr>
            <th>Recordings</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/recordings/1089_134686_000002_000000.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/recordings/2300_131720_000002_000001.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/recordings/3570_5694_000005_000003.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/recordings/4446_2275_000001_000000.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>FastFit</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/proposed/1089_134686_000002_000000.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/proposed/2300_131720_000002_000001.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/proposed/3570_5694_000005_000003.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/proposed/4446_2275_000001_000000.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>FastFit (U-Net)</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/u-net/1089_134686_000002_000000.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/u-net/2300_131720_000002_000001.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/u-net/3570_5694_000005_000003.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/u-net/4446_2275_000001_000000.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>Without AdaLN</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/wo-adaln/1089_134686_000002_000000.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/wo-adaln/2300_131720_000002_000001.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/wo-adaln/3570_5694_000005_000003.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/wo-adaln/4446_2275_000001_000000.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>Without skip-connections</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/wo-skip-connection/1089_134686_000002_000000.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/wo-skip-connection/2300_131720_000002_000001.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/wo-skip-connection/3570_5694_000005_000003.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/wo-skip-connection/4446_2275_000001_000000.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>Initial point from spectral envelope</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/spec-env/1089_134686_000002_000000.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/spec-env/2300_131720_000002_000001.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/spec-env/3570_5694_000005_000003.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/spec-env/4446_2275_000001_000000.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>Initial point from Griffin-Lim</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/griffin-lim/1089_134686_000002_000000.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/griffin-lim/2300_131720_000002_000001.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/griffin-lim/3570_5694_000005_000003.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/griffin-lim/4446_2275_000001_000000.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <th>Magnitude STFT encoder</th>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/proposed-mag/1089_134686_000002_000000.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/proposed-mag/2300_131720_000002_000001.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/proposed-mag/3570_5694_000005_000003.wav" type="audio/wav"></audio></td>
            <td><audio controls style="width: 150px;"><source src="wav_for_demo/ablation-study/proposed-mag/4446_2275_000001_000000.wav" type="audio/wav"></audio></td>
        </tr>
    </tbody>
</table>
