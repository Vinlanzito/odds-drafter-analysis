import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.stats import linregress
from scipy import stats
from statsmodels.stats.diagnostic import het_breuschpagan
import statsmodels.api as sm


# Read both Excel sheets into DataFrames
main = pd.read_excel('SheetJSTable.xlsx', sheet_name='Sheet1')  
rb = pd.read_excel('SheetJSTable.xlsx', sheet_name='Sheet2')
wr = pd.read_excel('SheetJSTable.xlsx', sheet_name='Sheet3')
te = pd.read_excel('SheetJSTable.xlsx', sheet_name='Sheet3')
qb = pd.read_excel('SheetJSTable.xlsx', sheet_name='Sheet4')

# Merge by a name
rb_df = pd.merge(main, rb, on='Name')
wr_df = pd.merge(main, wr, on='Name')  
te_df = pd.merge(main, te, on='Name') 
qb_df = pd.merge(main, qb, on='Name') 

rb_df = rb_df[rb_df['Position'] == 'RB']
rb_df = rb_df[rb_df['Rushing Yds'] > 0]
rb_df = rb_df[rb_df['G'] > 8]
rb_df = rb_df.sort_values(by='Rushing Yds', ascending=False)
wr_df = wr_df[wr_df['Position'] == 'WR']
wr_df = wr_df[wr_df['Receiving Yds'] > 0]
wr_df = wr_df[wr_df['G'] > 8]
wr_df = wr_df.sort_values(by='Receiving Yds', ascending=False)
te_df = te_df[te_df['Position'] == 'TE']
te_df = te_df[te_df['Receiving Yds'] > 0]
te_df = te_df[te_df['G'] > 8]
te_df = te_df.sort_values(by='Receiving Yds', ascending=False)
qb_df = qb_df[qb_df['Position'] == 'QB']
qb_df = qb_df[qb_df['Passing Yds'] > 0]
qb_df = qb_df[qb_df['G'] > 8]
qb_df = qb_df.sort_values(by='Passing Yds', ascending=False)

# Save the combined DataFrame to a new Excel file
rb_df.to_excel('rb_file.xlsx', index=False)
wr_df.to_excel('wr_file.xlsx', index=False)
te_df.to_excel('te_file.xlsx', index=False)
qb_df.to_excel('qb_file.xlsx', index=False)

script_dir = os.path.dirname(os.path.abspath(__file__))
images_path = os.path.join(script_dir, "images")

# RB plots

slope, intercept, r_value, p_value, std_err = linregress(rb_df['Rushing Yds'], rb_df['Yds'])
y_pred = rb_df['Rushing Yds'] * slope + intercept

dfPos = rb_df[rb_df['Yds'] > rb_df['Rushing Yds']]
dfNeg = rb_df[rb_df['Yds'] <= rb_df['Rushing Yds']]
plt.scatter(dfPos['Rushing Yds'], dfPos['Yds'], color='green')
plt.scatter(dfNeg['Rushing Yds'], dfNeg['Yds'], color='red')
#plt.scatter(rb_df['Rushing Yds'], rb_df['Yds'])
plt.plot(rb_df['Rushing Yds'], y_pred)
plt.xlabel("Projected Rushing")
plt.ylabel("Actual Rushing")
plt.title("Projected vs Actual Rushing Yards")

plt.savefig(os.path.join(images_path, 'rb_yards.png'))
plt.close()

print('Projected vs Actual Rushing Yards')
print(f"Correlation coefficient (r): {r_value:.2f}")
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"STD Error: {std_err:.2f}")


slope, intercept, r_value, p_value, std_err = linregress(rb_df['Rushing Yds'], rb_df['Y/G']*17)
y_pred = rb_df['Rushing Yds'] * slope + intercept

plt.scatter(rb_df['Rushing Yds'], rb_df['Y/G']*17)
plt.plot(rb_df['Rushing Yds'], y_pred)
plt.xlabel("Projected Rushing")
plt.ylabel("Actual Rushing")
plt.title("Projected vs Actual Rushing Yards per Game")

plt.savefig(os.path.join(images_path, 'rb_yardspg.png'))
plt.close()

print('Projected vs Actual Rushing Yards per Game')
print(f"Correlation coefficient (r): {r_value:.2f}")
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"STD Error: {std_err:.2f}")

# WR plots

slope, intercept, r_value, p_value, std_err = linregress(wr_df['Receiving Yds'], wr_df['Yds'])
y_pred = wr_df['Receiving Yds'] * slope + intercept

dfPos = wr_df[wr_df['Yds'] > wr_df['Receiving Yds']]
dfNeg = wr_df[wr_df['Yds'] <= wr_df['Receiving Yds']]
plt.scatter(dfPos['Receiving Yds'], dfPos['Yds'], color='green')
plt.scatter(dfNeg['Receiving Yds'], dfNeg['Yds'], color='red')
#plt.scatter(wr_df['Receiving Yds'], wr_df['Yds'])
plt.plot(wr_df['Receiving Yds'], y_pred)
plt.xlabel("Projected Receiving")
plt.ylabel("Actual Receiving")
plt.title("Projected vs Actual Receiving Yards (WR)")

plt.savefig(os.path.join(images_path, 'wr_yards.png'))
plt.close()

print('Projected vs Actual Receiving Yards (WR)')
print(f"Correlation coefficient (r): {r_value:.2f}")
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"STD Error: {std_err:.2f}")


slope, intercept, r_value, p_value, std_err = linregress(wr_df['Receiving Yds'], wr_df['Y/G']*17)
y_pred = wr_df['Receiving Yds'] * slope + intercept

plt.scatter(wr_df['Receiving Yds'], wr_df['Y/G']*17)
plt.plot(wr_df['Receiving Yds'], y_pred)
plt.xlabel("Projected Receiving")
plt.ylabel("Actual Receiving")
plt.title("Projected vs Actual Receiving Yards per Game (WR)")

plt.savefig(os.path.join(images_path, 'wr_yardspg.png'))
plt.close()

print('Projected vs Actual Receiving Yards per Game (WR)')
print(f"Correlation coefficient (r): {r_value:.2f}")
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"STD Error: {std_err:.2f}")


slope, intercept, r_value, p_value, std_err = linregress(wr_df['TDs'], wr_df['TD'])
y_pred = wr_df['TDs'] * slope + intercept

dfPos = wr_df[wr_df['TD'] > wr_df['TDs']]
dfNeg = wr_df[wr_df['TD'] <= wr_df['TDs']]
plt.scatter(dfPos['TDs'], dfPos['TD'], color='green')
plt.scatter(dfNeg['TDs'], dfNeg['TD'], color='red')
#plt.scatter(wr_df['TDs'], wr_df['TD'])
plt.plot(wr_df['TDs'], y_pred)
plt.xlabel("Projected TDs")
plt.ylabel("Actual TDs")
plt.title("Projected vs Actual Receiving TDs (WR)")

plt.savefig(os.path.join(images_path, 'wr_tds.png'))
plt.close()

print('Projected vs Actual Receiving TDs (WR)')
print(f"Correlation coefficient (r): {r_value:.2f}")
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"STD Error: {std_err:.2f}")


slope, intercept, r_value, p_value, std_err = linregress(wr_df['TDs'], wr_df['TD']/wr_df['G']*17)
y_pred = wr_df['TDs'] * slope + intercept

plt.scatter(wr_df['TDs'], wr_df['TD']/wr_df['G']*17)
plt.plot(wr_df['TDs'], y_pred)
plt.xlabel("Projected TDs")
plt.ylabel("Actual TDs")
plt.title("Projected vs Actual Receiving TDs per Game (WR)")

plt.savefig(os.path.join(images_path, 'wr_tdspg.png'))
plt.close()

print('Projected vs Actual Receiving TDs per Game (WR)')
print(f"Correlation coefficient (r): {r_value:.2f}")
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"STD Error: {std_err:.2f}")

# TE plots

slope, intercept, r_value, p_value, std_err = linregress(te_df['Receiving Yds'], te_df['Yds'])
y_pred = te_df['Receiving Yds'] * slope + intercept

dfPos = te_df[te_df['Yds'] > te_df['Receiving Yds']]
dfNeg = te_df[te_df['Yds'] <= te_df['Receiving Yds']]
plt.scatter(dfPos['Receiving Yds'], dfPos['Yds'], color='green')
plt.scatter(dfNeg['Receiving Yds'], dfNeg['Yds'], color='red')
#plt.scatter(te_df['Receiving Yds'], te_df['Yds'])
plt.plot(te_df['Receiving Yds'], y_pred)
plt.xlabel("Projected Receiving")
plt.ylabel("Actual Receiving")
plt.title("Projected vs Actual Receiving Yards (TE)")

plt.savefig(os.path.join(images_path, 'te_yards.png'))
plt.close()

print('Projected vs Actual Receiving Yards (TE)')
print(f"Correlation coefficient (r): {r_value:.2f}")
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"STD Error: {std_err:.2f}")


slope, intercept, r_value, p_value, std_err = linregress(te_df['Receiving Yds'], te_df['Y/G']*17)
y_pred = te_df['Receiving Yds'] * slope + intercept

plt.scatter(te_df['Receiving Yds'], te_df['Y/G']*17)
plt.plot(te_df['Receiving Yds'], y_pred)
plt.xlabel("Projected Receiving")
plt.ylabel("Actual Receiving")
plt.title("Projected vs Actual Receiving Yards per Game (TE)")

plt.savefig(os.path.join(images_path, 'te_yardspg.png'))
plt.close()

print('Projected vs Actual Receiving Yards per Game (TE)')
print(f"Correlation coefficient (r): {r_value:.2f}")
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"STD Error: {std_err:.2f}")


slope, intercept, r_value, p_value, std_err = linregress(te_df['TDs'], te_df['TD'])
y_pred = te_df['TDs'] * slope + intercept

dfPos = te_df[te_df['TD'] > te_df['TDs']]
dfNeg = te_df[te_df['TD'] <= te_df['TDs']]
plt.scatter(dfPos['TDs'], dfPos['TD'], color='green')
plt.scatter(dfNeg['TDs'], dfNeg['TD'], color='red')
#plt.scatter(te_df['TDs'], te_df['TD'])
plt.plot(te_df['TDs'], y_pred)
plt.xlabel("Projected TDs")
plt.ylabel("Actual TDs")
plt.title("Projected vs Actual Receiving TDs (TE)")

plt.savefig(os.path.join(images_path, 'te_tds.png'))
plt.close()

print('Projected vs Actual Receiving TDs (TE)')
print(f"Correlation coefficient (r): {r_value:.2f}")
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"STD Error: {std_err:.2f}")


slope, intercept, r_value, p_value, std_err = linregress(te_df['TDs'], te_df['TD']/te_df['G']*17)
y_pred = te_df['TDs'] * slope + intercept

plt.scatter(te_df['TDs'], te_df['TD']/te_df['G']*17)
plt.plot(te_df['TDs'], y_pred)
plt.xlabel("Projected TDs")
plt.ylabel("Actual TDs")
plt.title("Projected vs Actual Receiving TDs per Game (TE)")

plt.savefig(os.path.join(images_path, 'te_tdspg.png'))
plt.close()

print('Projected vs Actual Receiving TDs per Game (TE)')
print(f"Correlation coefficient (r): {r_value:.2f}")
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"STD Error: {std_err:.2f}")

# QB plots

slope, intercept, r_value, p_value, std_err = linregress(qb_df['Passing Yds'], qb_df['Yds'])
y_pred = qb_df['Passing Yds'] * slope + intercept

dfPos = qb_df[qb_df['Yds'] > qb_df['Passing Yds']]
dfNeg = qb_df[qb_df['Yds'] <= qb_df['Passing Yds']]
plt.scatter(dfPos['Passing Yds'], dfPos['Yds'], color='green')
plt.scatter(dfNeg['Passing Yds'], dfNeg['Yds'], color='red')
#plt.scatter(qb_df['Passing Yds'], qb_df['Yds'])
plt.plot(qb_df['Passing Yds'], y_pred)
plt.xlabel("Projected Passing")
plt.ylabel("Actual Passing")
plt.title("Projected vs Actual Passing Yards")

plt.savefig(os.path.join(images_path, 'qb_yards.png'))
plt.close()

print('Projected vs Actual Passing Yards')
print(f"Correlation coefficient (r): {r_value:.2f}")
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"STD Error: {std_err:.2f}")


slope, intercept, r_value, p_value, std_err = linregress(qb_df['Passing Yds'], qb_df['Y/G']*17)
y_pred = qb_df['Passing Yds'] * slope + intercept

plt.scatter(qb_df['Passing Yds'], qb_df['Y/G']*17)
plt.plot(qb_df['Passing Yds'], y_pred)
plt.xlabel("Projected Passing")
plt.ylabel("Actual Passing")
plt.title("Projected vs Actual Passing Yards per Game")

plt.savefig(os.path.join(images_path, 'qb_yardspg.png'))
plt.close()

print('Projected vs Actual Passing Yards per Game')
print(f"Correlation coefficient (r): {r_value:.2f}")
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"STD Error: {std_err:.2f}")


slope, intercept, r_value, p_value, std_err = linregress(qb_df['Passing TDs'], qb_df['TD'])
y_pred = qb_df['Passing TDs'] * slope + intercept

dfPos = qb_df[qb_df['TD'] > qb_df['Passing TDs']]
dfNeg = qb_df[qb_df['TD'] <= qb_df['Passing TDs']]
plt.scatter(dfPos['Passing TDs'], dfPos['TD'], color='green')
plt.scatter(dfNeg['Passing TDs'], dfNeg['TD'], color='red')
#plt.scatter(qb_df['Passing TDs'], qb_df['TD'])
plt.plot(qb_df['Passing TDs'], y_pred)
plt.xlabel("Projected TDs")
plt.ylabel("Actual TDs")
plt.title("Projected vs Actual Passing TDs (QB)")

plt.savefig(os.path.join(images_path, 'qb_tds.png'))
plt.close()

print('Projected vs Actual Passing TDs')
print(f"Correlation coefficient (r): {r_value:.2f}")
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"STD Error: {std_err:.2f}")


slope, intercept, r_value, p_value, std_err = linregress(qb_df['Passing TDs'], qb_df['TD']/qb_df['G']*17)
y_pred = qb_df['Passing TDs'] * slope + intercept

plt.scatter(qb_df['Passing TDs'], qb_df['TD']/qb_df['G']*17)
plt.plot(qb_df['Passing TDs'], y_pred)
plt.xlabel("Projected TDs")
plt.ylabel("Actual TDs")
plt.title("Projected vs Actual Passing TDs per Game")

plt.savefig(os.path.join(images_path, 'qb_tdspg.png'))
plt.close()

print('Projected vs Actual Passing TDs per Game')
print(f"Correlation coefficient (r): {r_value:.2f}")
print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
print(f"STD Error: {std_err:.2f}")


# Resisdual plots
# RB

mean = (rb_df['Yds']-rb_df['Rushing Yds']).mean();
corr_coef, p_value = stats.pearsonr(rb_df['Yds']-rb_df['Rushing Yds'], rb_df['Rushing Yds'])
X = sm.add_constant(rb_df['Rushing Yds'])
bp_test = het_breuschpagan(rb_df['Yds']-rb_df['Rushing Yds'], X)
shapiro_test = stats.shapiro(rb_df['Yds']-rb_df['Rushing Yds'])
skewness = stats.skew(rb_df['Yds']-rb_df['Rushing Yds'])

plt.scatter(rb_df['Rushing Yds'], rb_df['Yds']-rb_df['Rushing Yds'])
plt.plot(rb_df['Rushing Yds'], rb_df['Rushing Yds']*0)
plt.xlabel("Projected Rushing")
plt.ylabel("Actual Rushing")
plt.title("Projected vs Actual Rushing Yards Residual")

plt.savefig(os.path.join(images_path, 'rb_yardsres.png'))
plt.close()

print('Projected vs Actual Rushing Yards Residual')
print(f"Mean Residual: {mean:.2f}")
print(f"Correlation with predictor (coef, p_val): {corr_coef:.2f}, {p_value:.2f}")
lm, lm_p, f, f_p = bp_test
print(f"Breusch–Pagan: LM={lm:.4f}, LM p={lm_p:.4f}, F={f:.4f}, F p={f_p:.4f}")
stat, p_val = shapiro_test
print(f"Shapiro-Wilk Test: stat={stat:.2f}, p={p_val:.2f}")
print(f"Skewness: {skewness:.2f}")


mean = (rb_df['Y/G']*17-rb_df['Rushing Yds']).mean();
corr_coef, p_value = stats.pearsonr(rb_df['Y/G']*17-rb_df['Rushing Yds'], rb_df['Rushing Yds'])
X = sm.add_constant(rb_df['Rushing Yds'])
bp_test = het_breuschpagan(rb_df['Y/G']*17-rb_df['Rushing Yds'], X)
shapiro_test = stats.shapiro(rb_df['Y/G']*17-rb_df['Rushing Yds'])
skewness = stats.skew(rb_df['Y/G']*17-rb_df['Rushing Yds'])

plt.scatter(rb_df['Rushing Yds'], rb_df['Y/G']*17-rb_df['Rushing Yds'])
plt.plot(rb_df['Rushing Yds'], rb_df['Rushing Yds']*0)
plt.xlabel("Projected Rushing")
plt.ylabel("Actual Rushing")
plt.title("Projected vs Actual Rushing Yards per Game Residual")

plt.savefig(os.path.join(images_path, 'rb_yardspgres.png'))
plt.close()

print('Projected vs Actual Rushing Yards per Game Residual')
print(f"Mean Residual: {mean:.2f}")
print(f"Correlation with predictor (coef, p_val): {corr_coef:.2f}, {p_value:.2f}")
lm, lm_p, f, f_p = bp_test
print(f"Breusch–Pagan: LM={lm:.4f}, LM p={lm_p:.4f}, F={f:.4f}, F p={f_p:.4f}")
stat, p_val = shapiro_test
print(f"Shapiro-Wilk Test: stat={stat:.2f}, p={p_val:.2f}")
print(f"Skewness: {skewness:.2f}")

# WR

mean = (wr_df['Yds']-wr_df['Receiving Yds']).mean();
corr_coef, p_value = stats.pearsonr(wr_df['Yds']-wr_df['Receiving Yds'], wr_df['Receiving Yds'])
X = sm.add_constant(wr_df['Receiving Yds'])
bp_test = het_breuschpagan(wr_df['Yds']-wr_df['Receiving Yds'], X)
shapiro_test = stats.shapiro(wr_df['Yds']-wr_df['Receiving Yds'])
skewness = stats.skew(wr_df['Yds']-wr_df['Receiving Yds'])

plt.scatter(wr_df['Receiving Yds'], wr_df['Yds']-wr_df['Receiving Yds'])
plt.plot(wr_df['Receiving Yds'], wr_df['Receiving Yds']*0)
plt.xlabel("Projected Receiving")
plt.ylabel("Actual Receiving")
plt.title("Projected vs Actual Receiving Yards Residual (WR)")

plt.savefig(os.path.join(images_path, 'wr_yardsres.png'))
plt.close()

print('Projected vs Actual Receiving Yards Residual (WR)')
print(f"Mean Residual: {mean:.2f}")
print(f"Correlation with predictor (coef, p_val): {corr_coef:.2f}, {p_value:.2f}")
lm, lm_p, f, f_p = bp_test
print(f"Breusch–Pagan: LM={lm:.4f}, LM p={lm_p:.4f}, F={f:.4f}, F p={f_p:.4f}")
stat, p_val = shapiro_test
print(f"Shapiro-Wilk Test: stat={stat:.2f}, p={p_val:.2f}")
print(f"Skewness: {skewness:.2f}")


mean = (wr_df['Y/G']*17-wr_df['Receiving Yds']).mean();
corr_coef, p_value = stats.pearsonr(wr_df['Y/G']*17-wr_df['Receiving Yds'], wr_df['Receiving Yds'])
X = sm.add_constant(wr_df['Receiving Yds'])
bp_test = het_breuschpagan(wr_df['Y/G']*17-wr_df['Receiving Yds'], X)
shapiro_test = stats.shapiro(wr_df['Y/G']*17-wr_df['Receiving Yds'])
skewness = stats.skew(wr_df['Y/G']*17-wr_df['Receiving Yds'])

plt.scatter(wr_df['Receiving Yds'], wr_df['Y/G']*17-wr_df['Receiving Yds'])
plt.plot(wr_df['Receiving Yds'], wr_df['Receiving Yds']*0)
plt.xlabel("Projected Receiving")
plt.ylabel("Actual Receiving")
plt.title("Projected vs Actual Receiving Yards per Game Residual (WR)")

plt.savefig(os.path.join(images_path, 'wr_yardspgres.png'))
plt.close()

print('Projected vs Actual Receiving Yards per Game Residual (WR)')
print(f"Mean Residual: {mean:.2f}")
print(f"Correlation with predictor (coef, p_val): {corr_coef:.2f}, {p_value:.2f}")
lm, lm_p, f, f_p = bp_test
print(f"Breusch–Pagan: LM={lm:.4f}, LM p={lm_p:.4f}, F={f:.4f}, F p={f_p:.4f}")
stat, p_val = shapiro_test
print(f"Shapiro-Wilk Test: stat={stat:.2f}, p={p_val:.2f}")
print(f"Skewness: {skewness:.2f}")


mean = (wr_df['TD']-wr_df['TDs']).mean();
corr_coef, p_value = stats.pearsonr(wr_df['TD']-wr_df['TDs'], wr_df['TDs'])
X = sm.add_constant(wr_df['TDs'])
bp_test = het_breuschpagan(wr_df['TD']-wr_df['TDs'], X)
shapiro_test = stats.shapiro(wr_df['TD']-wr_df['TDs'])
skewness = stats.skew(wr_df['TD']-wr_df['TDs'])

plt.scatter(wr_df['TDs'], wr_df['TD']-wr_df['TDs'])
plt.plot(wr_df['TDs'], wr_df['TDs']*0)
plt.xlabel("Projected TDs")
plt.ylabel("Actual TDs")
plt.title("Projected vs Actual Receiving TDs Residual (WR)")

plt.savefig(os.path.join(images_path, 'wr_tdsres.png'))
plt.close()

print('Projected vs Actual Receiving TDs Residual (WR)')
print(f"Mean Residual: {mean:.2f}")
print(f"Correlation with predictor (coef, p_val): {corr_coef:.2f}, {p_value:.2f}")
lm, lm_p, f, f_p = bp_test
print(f"Breusch–Pagan: LM={lm:.4f}, LM p={lm_p:.4f}, F={f:.4f}, F p={f_p:.4f}")
stat, p_val = shapiro_test
print(f"Shapiro-Wilk Test: stat={stat:.2f}, p={p_val:.2f}")
print(f"Skewness: {skewness:.2f}")


mean = (wr_df['TD']/wr_df['G']*17-wr_df['TDs']).mean();
corr_coef, p_value = stats.pearsonr(wr_df['TD']/wr_df['G']*17-wr_df['TDs'], wr_df['TDs'])
X = sm.add_constant(wr_df['TDs'])
bp_test = het_breuschpagan(wr_df['TD']/wr_df['G']*17-wr_df['TDs'], X)
shapiro_test = stats.shapiro(wr_df['TD']/wr_df['G']*17-wr_df['TDs'])
skewness = stats.skew(wr_df['TD']/wr_df['G']*17-wr_df['TDs'])

plt.scatter(wr_df['TDs'], wr_df['TD']/wr_df['G']*17-wr_df['TDs'])
plt.plot(wr_df['TDs'], wr_df['TDs']*0)
plt.xlabel("Projected TDs")
plt.ylabel("Actual TDs")
plt.title("Projected vs Actual Receiving TDs per Game Residual (WR)")

plt.savefig(os.path.join(images_path, 'wr_tdspgres.png'))
plt.close()

print('Projected vs Actual Receiving TDs per Game Residual (WR)')
print(f"Mean Residual: {mean:.2f}")
print(f"Correlation with predictor (coef, p_val): {corr_coef:.2f}, {p_value:.2f}")
lm, lm_p, f, f_p = bp_test
print(f"Breusch–Pagan: LM={lm:.4f}, LM p={lm_p:.4f}, F={f:.4f}, F p={f_p:.4f}")
stat, p_val = shapiro_test
print(f"Shapiro-Wilk Test: stat={stat:.2f}, p={p_val:.2f}")
print(f"Skewness: {skewness:.2f}")


# TE

mean = (te_df['Yds']-te_df['Receiving Yds']).mean();
corr_coef, p_value = stats.pearsonr(te_df['Yds']-te_df['Receiving Yds'], te_df['Receiving Yds'])
X = sm.add_constant(te_df['Receiving Yds'])
bp_test = het_breuschpagan(te_df['Yds']-te_df['Receiving Yds'], X)
shapiro_test = stats.shapiro(te_df['Yds']-te_df['Receiving Yds'])
skewness = stats.skew(te_df['Yds']-te_df['Receiving Yds'])

plt.scatter(te_df['Receiving Yds'], te_df['Yds']-te_df['Receiving Yds'])
plt.plot(te_df['Receiving Yds'], te_df['Receiving Yds']*0)
plt.xlabel("Projected Receiving")
plt.ylabel("Actual Receiving")
plt.title("Projected vs Actual Receiving Yards Residual (TE)")

plt.savefig(os.path.join(images_path, 'te_yardsres.png'))
plt.close()

print('Projected vs Actual Receiving Yards Residual (TE)')
print(f"Mean Residual: {mean:.2f}")
print(f"Correlation with predictor (coef, p_val): {corr_coef:.2f}, {p_value:.2f}")
lm, lm_p, f, f_p = bp_test
print(f"Breusch–Pagan: LM={lm:.4f}, LM p={lm_p:.4f}, F={f:.4f}, F p={f_p:.4f}")
stat, p_val = shapiro_test
print(f"Shapiro-Wilk Test: stat={stat:.2f}, p={p_val:.2f}")
print(f"Skewness: {skewness:.2f}")


mean = (te_df['Y/G']*17-te_df['Receiving Yds']).mean();
corr_coef, p_value = stats.pearsonr(te_df['Y/G']*17-te_df['Receiving Yds'], te_df['Receiving Yds'])
X = sm.add_constant(te_df['Receiving Yds'])
bp_test = het_breuschpagan(te_df['Y/G']*17-te_df['Receiving Yds'], X)
shapiro_test = stats.shapiro(te_df['Y/G']*17-te_df['Receiving Yds'])
skewness = stats.skew(te_df['Y/G']*17-te_df['Receiving Yds'])

plt.scatter(te_df['Receiving Yds'], te_df['Y/G']*17-te_df['Receiving Yds'])
plt.plot(te_df['Receiving Yds'], te_df['Receiving Yds']*0)
plt.xlabel("Projected Receiving")
plt.ylabel("Actual Receiving")
plt.title("Projected vs Actual Receiving Yards per Game Residual (TE)")

plt.savefig(os.path.join(images_path, 'te_yardspgres.png'))
plt.close()

print('Projected vs Actual Receiving Yards per Game Residual (TE)')
print(f"Mean Residual: {mean:.2f}")
print(f"Correlation with predictor (coef, p_val): {corr_coef:.2f}, {p_value:.2f}")
lm, lm_p, f, f_p = bp_test
print(f"Breusch–Pagan: LM={lm:.4f}, LM p={lm_p:.4f}, F={f:.4f}, F p={f_p:.4f}")
stat, p_val = shapiro_test
print(f"Shapiro-Wilk Test: stat={stat:.2f}, p={p_val:.2f}")
print(f"Skewness: {skewness:.2f}")


mean = (te_df['TD']-te_df['TDs']).mean();
corr_coef, p_value = stats.pearsonr(te_df['TD']-te_df['TDs'], te_df['TDs'])
X = sm.add_constant(te_df['TDs'])
bp_test = het_breuschpagan(te_df['TD']-te_df['TDs'], X)
shapiro_test = stats.shapiro(te_df['TD']-te_df['TDs'])
skewness = stats.skew(te_df['TD']-te_df['TDs'])

plt.scatter(te_df['TDs'], te_df['TD']-te_df['TDs'])
plt.plot(te_df['TDs'], te_df['TDs']*0)
plt.xlabel("Projected TDs")
plt.ylabel("Actual TDs")
plt.title("Projected vs Actual Receiving TDs Residual (TE)")

plt.savefig(os.path.join(images_path, 'te_tdsres.png'))
plt.close()

print('Projected vs Actual Receiving TDs Residual (TE)')
print(f"Mean Residual: {mean:.2f}")
print(f"Correlation with predictor (coef, p_val): {corr_coef:.2f}, {p_value:.2f}")
lm, lm_p, f, f_p = bp_test
print(f"Breusch–Pagan: LM={lm:.4f}, LM p={lm_p:.4f}, F={f:.4f}, F p={f_p:.4f}")
stat, p_val = shapiro_test
print(f"Shapiro-Wilk Test: stat={stat:.2f}, p={p_val:.2f}")
print(f"Skewness: {skewness:.2f}")


mean = (te_df['TD']/te_df['G']*17-te_df['TDs']).mean();
corr_coef, p_value = stats.pearsonr(te_df['TD']/te_df['G']*17-te_df['TDs'], te_df['TDs'])
X = sm.add_constant(te_df['TDs'])
bp_test = het_breuschpagan(te_df['TD']/te_df['G']*17-te_df['TDs'], X)
shapiro_test = stats.shapiro(te_df['TD']/te_df['G']*17-te_df['TDs'])
skewness = stats.skew(te_df['TD']/te_df['G']*17-te_df['TDs'])

plt.scatter(te_df['TDs'], te_df['TD']/te_df['G']*17-te_df['TDs'])
plt.plot(te_df['TDs'], te_df['TDs']*0)
plt.xlabel("Projected TDs")
plt.ylabel("Actual TDs")
plt.title("Projected vs Actual Receiving TDs per Game Residual (TE)")

plt.savefig(os.path.join(images_path, 'te_tdspgres.png'))
plt.close()

print('Projected vs Actual Receiving TDs per Game Residual (TE)')
print(f"Mean Residual: {mean:.2f}")
print(f"Correlation with predictor (coef, p_val): {corr_coef:.2f}, {p_value:.2f}")
lm, lm_p, f, f_p = bp_test
print(f"Breusch–Pagan: LM={lm:.4f}, LM p={lm_p:.4f}, F={f:.4f}, F p={f_p:.4f}")
stat, p_val = shapiro_test
print(f"Shapiro-Wilk Test: stat={stat:.2f}, p={p_val:.2f}")
print(f"Skewness: {skewness:.2f}")


# QB

mean = (qb_df['Yds']-qb_df['Passing Yds']).mean();
corr_coef, p_value = stats.pearsonr(qb_df['Yds']-qb_df['Passing Yds'], qb_df['Passing Yds'])
X = sm.add_constant(qb_df['Passing Yds'])
bp_test = het_breuschpagan(qb_df['Yds']-qb_df['Passing Yds'], X)
shapiro_test = stats.shapiro(qb_df['Yds']-qb_df['Passing Yds'])
skewness = stats.skew(qb_df['Yds']-qb_df['Passing Yds'])

plt.scatter(qb_df['Passing Yds'], qb_df['Yds']-qb_df['Passing Yds'])
plt.plot(qb_df['Passing Yds'], qb_df['Passing Yds']*0)
plt.xlabel("Projected Passing")
plt.ylabel("Actual Passing")
plt.title("Projected vs Actual Passing Yards Residual")

plt.savefig(os.path.join(images_path, 'qb_yardsres.png'))
plt.close()

print('Projected vs Actual Passing Yards Residual')
print(f"Mean Residual: {mean:.2f}")
print(f"Correlation with predictor (coef, p_val): {corr_coef:.2f}, {p_value:.2f}")
lm, lm_p, f, f_p = bp_test
print(f"Breusch–Pagan: LM={lm:.4f}, LM p={lm_p:.4f}, F={f:.4f}, F p={f_p:.4f}")
stat, p_val = shapiro_test
print(f"Shapiro-Wilk Test: stat={stat:.2f}, p={p_val:.2f}")
print(f"Skewness: {skewness:.2f}")


mean = (qb_df['Y/G']*17-qb_df['Passing Yds']).mean();
corr_coef, p_value = stats.pearsonr(qb_df['Y/G']*17-qb_df['Passing Yds'], qb_df['Passing Yds'])
X = sm.add_constant(qb_df['Passing Yds'])
bp_test = het_breuschpagan(qb_df['Y/G']*17-qb_df['Passing Yds'], X)
shapiro_test = stats.shapiro(qb_df['Y/G']*17-qb_df['Passing Yds'])
skewness = stats.skew(qb_df['Y/G']*17-qb_df['Passing Yds'])

plt.scatter(qb_df['Passing Yds'], qb_df['Y/G']*17-qb_df['Passing Yds'])
plt.plot(qb_df['Passing Yds'], qb_df['Passing Yds']*0)
plt.xlabel("Projected Passing")
plt.ylabel("Actual Passing")
plt.title("Projected vs Actual Passing Yards per Game Residual")

plt.savefig(os.path.join(images_path, 'qb_yardspgres.png'))
plt.close()

print('Projected vs Actual Passing Yards per Game Residual')
print(f"Mean Residual: {mean:.2f}")
print(f"Correlation with predictor (coef, p_val): {corr_coef:.2f}, {p_value:.2f}")
lm, lm_p, f, f_p = bp_test
print(f"Breusch–Pagan: LM={lm:.4f}, LM p={lm_p:.4f}, F={f:.4f}, F p={f_p:.4f}")
stat, p_val = shapiro_test
print(f"Shapiro-Wilk Test: stat={stat:.2f}, p={p_val:.2f}")
print(f"Skewness: {skewness:.2f}")


mean = (qb_df['TD']-qb_df['Passing TDs']).mean();
corr_coef, p_value = stats.pearsonr(qb_df['TD']-qb_df['Passing TDs'], qb_df['Passing TDs'])
X = sm.add_constant(qb_df['Passing TDs'])
bp_test = het_breuschpagan(qb_df['TD']-qb_df['Passing TDs'], X)
shapiro_test = stats.shapiro(qb_df['TD']-qb_df['Passing TDs'])
skewness = stats.skew(qb_df['TD']-qb_df['Passing TDs'])

plt.scatter(qb_df['Passing TDs'], qb_df['TD']-qb_df['Passing TDs'])
plt.plot(qb_df['Passing TDs'], qb_df['Passing TDs']*0)
plt.xlabel("Projected TDs")
plt.ylabel("Actual TDs")
plt.title("Projected vs Actual Passing TDs Residual")

plt.savefig(os.path.join(images_path, 'qb_tdsres.png'))
plt.close()

print('Projected vs Actual Passing TDs Residual')
print(f"Mean Residual: {mean:.2f}")
print(f"Correlation with predictor (coef, p_val): {corr_coef:.2f}, {p_value:.2f}")
lm, lm_p, f, f_p = bp_test
print(f"Breusch–Pagan: LM={lm:.4f}, LM p={lm_p:.4f}, F={f:.4f}, F p={f_p:.4f}")
stat, p_val = shapiro_test
print(f"Shapiro-Wilk Test: stat={stat:.2f}, p={p_val:.2f}")
print(f"Skewness: {skewness:.2f}")


mean = (qb_df['TD']/qb_df['G']*17-qb_df['Passing TDs']).mean();
corr_coef, p_value = stats.pearsonr(qb_df['TD']/qb_df['G']*17-qb_df['Passing TDs'], qb_df['Passing TDs'])
X = sm.add_constant(qb_df['Passing TDs'])
bp_test = het_breuschpagan(qb_df['TD']/qb_df['G']*17-qb_df['Passing TDs'], X)
shapiro_test = stats.shapiro(qb_df['TD']/qb_df['G']*17-qb_df['Passing TDs'])
skewness = stats.skew(qb_df['TD']/qb_df['G']*17-qb_df['Passing TDs'])

plt.scatter(qb_df['Passing TDs'], qb_df['TD']/qb_df['G']*17-qb_df['Passing TDs'])
plt.plot(qb_df['Passing TDs'], qb_df['Passing TDs']*0)
plt.xlabel("Projected TDs")
plt.ylabel("Actual TDs")
plt.title("Projected vs Actual Passing TDs per Game Residual")

plt.savefig(os.path.join(images_path, 'qb_tdspgres.png'))
plt.close()

print('Projected vs Actual Passing TDs per Game Residual')
print(f"Mean Residual: {mean:.2f}")
print(f"Correlation with predictor (coef, p_val): {corr_coef:.2f}, {p_value:.2f}")
lm, lm_p, f, f_p = bp_test
print(f"Breusch–Pagan: LM={lm:.4f}, LM p={lm_p:.4f}, F={f:.4f}, F p={f_p:.4f}")
stat, p_val = shapiro_test
print(f"Shapiro-Wilk Test: stat={stat:.2f}, p={p_val:.2f}")
print(f"Skewness: {skewness:.2f}")