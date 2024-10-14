/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
const createCounter = function (init) {
    let initial = init;
    return {
        increment: () => {
            return ++initial;
        },
        decrement: () => {
            return --initial;
        },
        reset: () => {
            return initial = init;
        }
    };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
