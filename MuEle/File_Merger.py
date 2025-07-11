import os
import sys

from Scripts.CreateListToRun import menu

clean=menu("Clean the output directories?",["No","Yes"])

if clean:
	os.system("rm MC/out/*.root")

channel_dir=os.getcwd()+'/'

samples_dir=sys.argv[1]

try :
	os.chdir(samples_dir)
	type_of_run = menu("Type of run...",["NOMINAL",'Systematics'])

	if type_of_run==1:
		os.system('hadd '+channel_dir+'MC/out/Signal_Sherpa.root NOMINAL/VBF_Ztautau_sherpa*.root')
		os.system('hadd '+channel_dir+'MC/out/Signal_PoPy.root NOMINAL/VBF_Ztautau_201*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/Ztautau_Sherpa.root NOMINAL/Ztautau_sherpa*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/Ztautau_PoPy.root NOMINAL/Ztautau_201*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/Ztautau_MG.root NOMINAL/Ztautau_MG[!NLO]*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/Ztautau_MGNLO.root NOMINAL/Ztautau_MGNLO*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/Ztautau_SherpaNLO.root NOMINAL/Ztautau_SherpaNLO*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/Zjets.root NOMINAL/Zmumu_201*.root NOMINAL/Zee_201*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/Higgs.root NOMINAL/WpH*.root NOMINAL/WmH*.root NOMINAL/ZHllbb*.root NOMINAL/ZHlltautau*.root NOMINAL/ggHttlm15hp20*.root NOMINAL/ggHttlp15hm20*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/Higgs_EWK.root NOMINAL/VBFHttlm15hp20*.root NOMINAL/VBFHttlp15hm20*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/VV.root NOMINAL/llll_*.root NOMINAL/lllv_*.root NOMINAL/llvv_*.root NOMINAL/lvvv_*.root NOMINAL/ZqqZvv_*.root NOMINAL/ZqqZll_*.root NOMINAL/WqqZvv_*.root NOMINAL/WqqZll_*.root NOMINAL/WlvZqq_*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/Wjets.root NOMINAL/Wplusenu_*.root NOMINAL/Wminusenu_*.root NOMINAL/Wplusmunu_*.root NOMINAL/Wminusmunu_*.root NOMINAL/Wplustaunu_*.root NOMINAL/Wminustaunu_*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/singletop.root NOMINAL/st_schan_top_*.root NOMINAL/st_schan_atop_*.root NOMINAL/st_tchan_top_*.root NOMINAL/st_tchan_atop_*.root NOMINAL/st_wt_top_*.root NOMINAL/st_wt_atop_*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/ttbar.root NOMINAL/ttbar_*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/W_EWK_Sherpa.root NOMINAL/W_EWK_sherpa*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/W_EWK_PoPy.root NOMINAL/W_EWK_PoPy*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/VV_EWK.root NOMINAL/VV_EWK*.root')
		os.system('hadd -j 4 '+channel_dir+'MC/out/data.root NOMINAL/data_*.root')

	elif type_of_run==2:
		for d in os.listdir():
			if d!="Systematics":
				os.system("hadd -j 10 Systematics/Signal_Sherpa_"+d+".root "+d+"/VBF_Ztautau*"+d+".root")
				os.system("hadd -j 10 Systematics/Ztautau_SherpaRW_"+d+".root "+d+"/Ztautau_sherpa*"+d+".root")

except FileNotFoundError :
	print("Non valid directory!")
	print("You are at ",os.getcwd())