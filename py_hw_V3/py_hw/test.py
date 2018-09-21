import extra_credit
import warmup
import sys
hw = extra_credit

KEY="COGS_3>>"

def run_test(fun,args,chk,pts):
    try:
        rv=fun(*args)
        print("%s calling %s(%s)... " % \
              #(KEY,fun.__name__,",".join([repr(x) for x in args])),rv)
              (KEY,fun.__name__,",".join([repr(x) for x in args])))
    except Exception as e:
        print("Exception: "+str(e))
        return 0
    else:
        if chk(rv):
            print("Passed")
            return pts
        else:
            print("Try Again")
            return 0

def chk_val(x):
    return lambda y: x==y

def chk_flt(x):
    return lambda y: abs(x-y)<1e-8

def chk_dict(qry,rslt,sz):
    return lambda d: len(d)==sz and qry in d and d[qry]==rslt

def chk_set(qry,sz):
    return lambda d: len(d)==sz and qry in d

def chk_file(fn):
    return lambda d: sys.stdout.write("\nSee file \"%s\"\n" % fn) or True

def run_tests(tests):
    score=0
    total=0
    for (fun,args,chk,pts) in tests:
        score+=run_test(fun,args,chk,pts)
        total+=pts
    return (score,total)

def run_all_tests():
    globals={}
    return run_tests([
        #problem 1
        # (misc.closest_to,[[2,4,8,9],7],chk_val(8),1),
        (warmup.fibo,[],chk_val(int('0x00466664', 16)), 5),
        (warmup.multiples_of_3_and_5,[],chk_val(int('0x00038ED0', 16)), 5),
        (warmup.collatz,[],chk_val(int('0x000CC8A7', 16)), 5),
        (hw.get_row_from_id,["A0027"],chk_val(["A0027", 16, 20, 19, 19]),10),
        (hw.get_row_from_id,["A0028"],chk_val(["A0028", 19, 0, 20, 20]),10),
        (hw.get_row_from_id,["AXXXXX"],chk_val(False),5),
        (hw.calc_avg_per_student,["A0009"],chk_flt(15.0),5),
        (hw.calc_avg_per_student,["A0006"],chk_flt(19.25),5),
        (hw.calc_avg_per_student,["A0016"],chk_flt(15.25),5),
        (hw.calc_avg_per_test,[0],chk_flt(15.717948717948717),5),
        (hw.calc_avg_per_test,[1],chk_flt(16.28205128205128),5),
        (hw.calc_avg_per_test,[2],chk_flt(16.71794871794872),5),
        (hw.calc_avg_per_test,[3],chk_val(False),5),
        (hw.get_name_from_id,['A0014'],chk_val('Barney Gumbell'),5),
        (hw.get_name_from_id,['A0010'],chk_val('Selma Bouvier'),5),
        (hw.get_name_from_id,['A0016'],chk_val('Lisa Simpson'),5),
        (hw.get_name_from_id,['A9900'],chk_val(False),5),
        (hw.print_grade_from_name,['Apu Nahasapeemapetilon'],chk_flt(15.0),5),
        (hw.print_grade_from_name,['Hans Molemen'],chk_flt(19.25),5),
        (hw.print_grade_from_name,['Montgomery Burns'],chk_flt(14.5),5),
        (hw.print_grade_from_name,['Jon Snow'],chk_val(False),5),
        ])

(s,t)=run_all_tests()
print("%s Results: (%d/%d)" % (KEY,s,t))
print("%s Compiled" % KEY)
