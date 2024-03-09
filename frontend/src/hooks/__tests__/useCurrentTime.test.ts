import { renderHook } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('test useCurrentTime hook', () => {
    it('should return current time', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toStrictEqual(
            new Date().toLocaleTimeString('ru-RU')
        );
    });
});
