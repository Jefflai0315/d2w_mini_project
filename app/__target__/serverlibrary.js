// Transcrypt'ed from Python, 2021-10-21 01:09:50
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = '__main__';
export var mergesort = function (array, byfunc) {
	if (typeof byfunc == 'undefined' || (byfunc != null && byfunc.hasOwnProperty ("__kwargtrans__"))) {;
		var byfunc = null;
	};
	if (len (array) > 1) {
		var n = Math.floor (len (array) / 2);
		var L = mergesort (array.__getslice__ (0, n, 1), byfunc);
		var R = mergesort (array.__getslice__ (n, null, 1), byfunc);
		var nleft = len (array.__getslice__ (0, n, 1));
		var nright = len (array.__getslice__ (n, null, 1));
		var left = 0;
		var right = 0;
		var dest = 0;
		while (left < nleft && right < nright) {
			if (byfunc (L [left]) <= byfunc (R [right])) {
				array [dest] = L [left];
				left++;
			}
			else {
				array [dest] = R [right];
				right++;
			}
			dest++;
		}
		while (left < nleft) {
			array [dest] = L [left];
			left++;
			dest++;
		}
		while (right < nright) {
			array [dest] = R [right];
			right++;
			dest++;
		}
	}
	return array;
};
export var Stack =  __class__ ('Stack', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		self.py_items = [];
	});},
	get push () {return __get__ (this, function (self, item) {
		self.py_items.append (item);
		return self.py_items;
	});},
	get py_pop () {return __get__ (this, function (self) {
		if (len (self.py_items) == 0) {
			return null;
		}
		else {
			return self.py_items.py_pop (-(1));
		}
	});},
	get peek () {return __get__ (this, function (self) {
		if (len (self.py_items) == 0) {
			return null;
		}
		else {
			return self.py_items [-(1)];
		}
	});},
	get _get_is_empty () {return __get__ (this, function (self) {
		return len (self.py_items) == 0;
	});},
	get _get_size () {return __get__ (this, function (self) {
		if (len (self.py_items) != 0) {
			return len (self.py_items);
		}
	});}
});
Object.defineProperty (Stack, 'size', property.call (Stack, Stack._get_size));
Object.defineProperty (Stack, 'is_empty', property.call (Stack, Stack._get_is_empty));;
export var EvaluateExpression =  __class__ ('EvaluateExpression', [object], {
	__module__: __name__,
	valid_char: '0123456789+-*/() ',
	get __init__ () {return __get__ (this, function (self, string) {
		if (typeof string == 'undefined' || (string != null && string.hasOwnProperty ("__kwargtrans__"))) {;
			var string = '';
		};
		self._expr = string;
	});},
	get _get_expression () {return __get__ (this, function (self) {
		return self._expr;
	});},
	get _set_expression () {return __get__ (this, function (self, new_expr) {
		for (var c of new_expr) {
			if (!__in__ (c, EvaluateExpression.valid_char)) {
				self._expr = '';
				print (self._expr + ' is wrong ');
				return str (self._expr);
			}
		}
		self._expr = new_expr;
		return self._expr;
	});},
	get insert_space () {return __get__ (this, function (self) {
		var ls = [];
		for (var i = 0; i < len (self._expr); i++) {
			if (__in__ (self._expr [i], '+-*/()')) {
				ls.extend (tuple ([' ', self._expr [i], ' ']));
			}
			else {
				ls.append (self._expr [i]);
			}
		}
		var string = ''.join (ls);
		return string;
	});},
	get process_operator () {return __get__ (this, function (self, operand_stack, operator_stack) {
		var R = operand_stack.py_pop ();
		var L = operand_stack.py_pop ();
		var op = operator_stack.py_pop ();
		if (op == '/') {
			var op = '//';
		}
		var result = eval (''.join (map (str, [L, op, R])));
		print (''.join (map (str, [L, op, R])));
		operand_stack.push (result);
	});},
	get evaluate () {return __get__ (this, function (self) {
		var operand_stack = Stack ();
		var operator_stack = Stack ();
		var expression = self.insert_space ();
		var tokens = expression.py_split ();
		print (expression, tokens);
		var operator = ['*', '/', '+', '-', '(', ')'];
		for (var c of tokens) {
			if (!__in__ (c, operator)) {
				operand_stack.push (c);
			}
			else if (__in__ (c, '+-')) {
				if (c == '-' && operand_stack.is_empty) {
					operand_stack.push (0);
				}
				while (!(operator_stack.is_empty) && !__in__ (operator_stack.peek (), '()')) {
					var R = operand_stack.py_pop ();
					var L = operand_stack.py_pop ();
					var op = operator_stack.py_pop ();
					if (op == '/') {
						var op = '//';
					}
					var result = eval (''.join (map (str, [L, op, R])));
					operand_stack.push (result);
				}
				operator_stack.push (c);
			}
			else if (__in__ (c, '*/')) {
				while (__in__ (operator_stack.peek (), '*/')) {
					var R = operand_stack.py_pop ();
					var L = operand_stack.py_pop ();
					var op = operator_stack.py_pop ();
					if (op == '/') {
						var op = '//';
					}
					var result = eval (''.join (map (str, [L, op, R])));
					operand_stack.push (result);
				}
				operator_stack.push (c);
			}
			else if (c == '(') {
				operator_stack.push (c);
			}
			else if (c == ')') {
				while (operator_stack.peek () != '(') {
					var R = operand_stack.py_pop ();
					var L = operand_stack.py_pop ();
					var op = operator_stack.py_pop ();
					if (op == '/') {
						var op = '//';
					}
					var result = eval (''.join (map (str, [L, op, R])));
					operand_stack.push (result);
				}
			}
		}
		print ('whats remaining: ', 'Operand: ', operand_stack._Stackpy_items, ' Operator: ', operator_stack._Stackpy_items);
		while (!(operator_stack.is_empty)) {
			if (__in__ (operator_stack.peek (), '()')) {
				operator_stack.py_pop ();
			}
			else {
				var R = operand_stack.py_pop ();
				var L = operand_stack.py_pop ();
				var op = operator_stack.py_pop ();
				if (op == '/') {
					var op = '//';
				}
				var result = eval (''.join (map (str, [L, op, R])));
				operand_stack.push (result);
			}
		}
		return operand_stack.py_pop ();
	});}
});
Object.defineProperty (EvaluateExpression, 'expression', property.call (EvaluateExpression, EvaluateExpression._get_expression, EvaluateExpression._set_expression));;
export var get_smallest_three = function (challenge) {
	var records = challenge.records;
	var times = (function () {
		var __accu0__ = [];
		for (var r of records) {
			__accu0__.append (r);
		}
		return __accu0__;
	}) ();
	mergesort (times, (function __lambda__ (x) {
		return x.elapsed_time;
	}));
	return times.__getslice__ (0, 3, 1);
};

//# sourceMappingURL=serverlibrary.map