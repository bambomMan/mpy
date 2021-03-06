
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left=left+-left*/rightUMINUSDEF ELIF ELSE FOR ID IF INT NUMBER WHILEstatement : INT ID statement : ID "=" expressionstatement : expression expression : expression \'+\' expression \n                  | expression \'-\' expression \n                  | expression \'*\' expression \n                  | expression \'/\' expressionexpression : \'-\' expression %prec UMINUSexpression : \'(\' expression \')\'expression : NUMBERexpression : ID'
    
_lr_action_items = {'INT':([0,],[2,]),'ID':([0,2,5,6,9,10,11,12,13,],[3,8,15,15,15,15,15,15,15,]),'-':([0,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,],[5,-11,11,5,5,-10,5,5,5,5,5,-8,-11,11,11,-4,-5,-6,-7,-9,]),'(':([0,5,6,9,10,11,12,13,],[6,6,6,6,6,6,6,6,]),'NUMBER':([0,5,6,9,10,11,12,13,],[7,7,7,7,7,7,7,7,]),'$end':([1,3,4,7,8,14,15,17,18,19,20,21,22,],[0,-11,-3,-10,-1,-8,-11,-2,-4,-5,-6,-7,-9,]),'=':([3,],[9,]),'+':([3,4,7,14,15,16,17,18,19,20,21,22,],[-11,10,-10,-8,-11,10,10,-4,-5,-6,-7,-9,]),'*':([3,4,7,14,15,16,17,18,19,20,21,22,],[-11,12,-10,-8,-11,12,12,12,12,-6,-7,-9,]),'/':([3,4,7,14,15,16,17,18,19,20,21,22,],[-11,13,-10,-8,-11,13,13,13,13,-6,-7,-9,]),')':([7,14,15,16,18,19,20,21,22,],[-10,-8,-11,22,-4,-5,-6,-7,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,5,6,9,10,11,12,13,],[4,14,16,17,18,19,20,21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> INT ID','statement',2,'p_statement_INT','calc.py',71),
  ('statement -> ID = expression','statement',3,'p_statement_assign','calc.py',77),
  ('statement -> expression','statement',1,'p_statement_expr','calc.py',83),
  ('expression -> expression + expression','expression',3,'p_expression_binop','calc.py',88),
  ('expression -> expression - expression','expression',3,'p_expression_binop','calc.py',89),
  ('expression -> expression * expression','expression',3,'p_expression_binop','calc.py',90),
  ('expression -> expression / expression','expression',3,'p_expression_binop','calc.py',91),
  ('expression -> - expression','expression',2,'p_expression_uminus','calc.py',103),
  ('expression -> ( expression )','expression',3,'p_expression_group','calc.py',108),
  ('expression -> NUMBER','expression',1,'p_expression_number','calc.py',113),
  ('expression -> ID','expression',1,'p_expression_id','calc.py',118),
]
