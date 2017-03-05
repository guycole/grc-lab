#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Feb 28 11:41:41 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.working_samp_rate = working_samp_rate = 400e3
        self.volume = volume = 1
        self.transition_width = transition_width = 10e3
        self.samp_rate = samp_rate = 8e6
        self.freq = freq = 94.9e6
        self.channel_width = channel_width = 150e3
        self.center_freq = center_freq = 96e6
        self.audio_cutoff = audio_cutoff = 20e3

        ##################################################
        # Blocks
        ##################################################
        self._volume_range = Range(0, 11, 1, 1, 200)
        self._volume_win = RangeWidget(self._volume_range, self.set_volume, "volume", "counter_slider", float)
        self.top_layout.addWidget(self._volume_win)
        self._freq_tool_bar = Qt.QToolBar(self)
        self._freq_tool_bar.addWidget(Qt.QLabel("freq"+": "))
        self._freq_line_edit = Qt.QLineEdit(str(self.freq))
        self._freq_tool_bar.addWidget(self._freq_line_edit)
        self._freq_line_edit.returnPressed.connect(
        	lambda: self.set_freq(eng_notation.str_to_num(str(self._freq_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._freq_tool_bar)
        self._center_freq_tool_bar = Qt.QToolBar(self)
        self._center_freq_tool_bar.addWidget(Qt.QLabel('center_freq'+": "))
        self._center_freq_line_edit = Qt.QLineEdit(str(self.center_freq))
        self._center_freq_tool_bar.addWidget(self._center_freq_line_edit)
        self._center_freq_line_edit.returnPressed.connect(
        	lambda: self.set_center_freq(eng_notation.str_to_num(str(self._center_freq_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._center_freq_tool_bar)
        self._audio_cutoff_tool_bar = Qt.QToolBar(self)
        self._audio_cutoff_tool_bar.addWidget(Qt.QLabel("audio_cutoff"+": "))
        self._audio_cutoff_line_edit = Qt.QLineEdit(str(self.audio_cutoff))
        self._audio_cutoff_tool_bar.addWidget(self._audio_cutoff_line_edit)
        self._audio_cutoff_line_edit.returnPressed.connect(
        	lambda: self.set_audio_cutoff(eng_notation.str_to_num(str(self._audio_cutoff_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._audio_cutoff_tool_bar)
        self.spectrum = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	samp_rate, #bw
        	'spectrum', #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.spectrum.set_update_time(1.0/10)
        self._spectrum_win = sip.wrapinstance(self.spectrum.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._spectrum_win)

        self.spectrum.enable_rf_freq(True)



        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=48000,
                decimation=int(working_samp_rate),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_sink_x_1_0 = qtgui.sink_f(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	working_samp_rate, #bw
        	'demod', #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_1_0.set_update_time(1.0/10)
        self._qtgui_sink_x_1_0_win = sip.wrapinstance(self.qtgui_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_1_0_win)

        self.qtgui_sink_x_1_0.enable_rf_freq(False)



        self.qtgui_sink_x_1 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	working_samp_rate, #bw
        	'FIR out', #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_1.set_update_time(1.0/10)
        self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_1_win)

        self.qtgui_sink_x_1.enable_rf_freq(False)



        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(center_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, working_samp_rate, audio_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(int(samp_rate/working_samp_rate), (firdes.low_pass(1, samp_rate, channel_width, transition_width)), freq - center_freq, samp_rate)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=working_samp_rate,
        	audio_decimation=1,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.qtgui_sink_x_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.qtgui_sink_x_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.spectrum, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_working_samp_rate(self):
        return self.working_samp_rate

    def set_working_samp_rate(self, working_samp_rate):
        self.working_samp_rate = working_samp_rate
        self.qtgui_sink_x_1_0.set_frequency_range(self.center_freq, self.working_samp_rate)
        self.qtgui_sink_x_1.set_frequency_range(self.center_freq, self.working_samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.working_samp_rate, self.audio_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))

    def get_transition_width(self):
        return self.transition_width

    def set_transition_width(self, transition_width):
        self.transition_width = transition_width
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1, self.samp_rate, self.channel_width, self.transition_width)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.spectrum.set_frequency_range(self.center_freq, self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1, self.samp_rate, self.channel_width, self.transition_width)))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        Qt.QMetaObject.invokeMethod(self._freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.freq)))
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.freq - self.center_freq)

    def get_channel_width(self):
        return self.channel_width

    def set_channel_width(self, channel_width):
        self.channel_width = channel_width
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1, self.samp_rate, self.channel_width, self.transition_width)))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        Qt.QMetaObject.invokeMethod(self._center_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.center_freq)))
        self.spectrum.set_frequency_range(self.center_freq, self.samp_rate)
        self.qtgui_sink_x_1_0.set_frequency_range(self.center_freq, self.working_samp_rate)
        self.qtgui_sink_x_1.set_frequency_range(self.center_freq, self.working_samp_rate)
        self.osmosdr_source_0.set_center_freq(self.center_freq, 0)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.freq - self.center_freq)

    def get_audio_cutoff(self):
        return self.audio_cutoff

    def set_audio_cutoff(self, audio_cutoff):
        self.audio_cutoff = audio_cutoff
        Qt.QMetaObject.invokeMethod(self._audio_cutoff_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.audio_cutoff)))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.working_samp_rate, self.audio_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
